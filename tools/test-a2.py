#!/usr/bin/env python3
# What: the Auditor's driver, first written for Test A2 and used through tools/test-a3.py for Exp 1: a blinded copy of
#   each run, the Auditor's first look, the runs it names (checked and listed for tools/run-named-runs.sh) and its
#   second look. A library: tools/test-a3.py calls it.
#   Cleaned copy of the driver used in the experiments: only the paths changed (relative to this repository, with
#   environment overrides), and the parts used only by experiments not released here are left out. The flags of the
#   agent call, the hint removal, the checks on named runs and the brief assembly are unchanged.
# Who runs it: no one directly; `python3 tools/test-a2.py` only checks the frozen briefs (auditor/SHA256SUMS).
# Refuses: to start if a frozen brief changed (auditor/SHA256SUMS); a named run whose NAME is not an index variable of
#   the input or its included setup, or whose total steps exceed four times the original's; a copy in which a hint
#   survives.
# Paths: TESTBED_RESULTS (the results folder; default results/), TESTBED_RUNS (default: cases/, the seed-11 runs),
#   TESTBED_COPIES (where the blinded copies are made; default /tmp/testbed-copies).
import concurrent.futures as cf
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent  # the repository root
# the results folder: holds reruns/ (the named runs' outputs) and reruns.txt (the list for tools/run-named-runs.sh).
# Default: the released results/. A new try goes in its own folder (TESTBED_RESULTS), so history stays as shipped.
T1 = Path(os.environ["TESTBED_RESULTS"]).resolve() if os.environ.get("TESTBED_RESULTS") else HERE / "results"
T2 = T1 / "test-a2"
IDS = HERE / "key" / "ids.txt"  # neutral id -> run label (sealed during the experiments, published here)
RUNS = Path(os.environ["TESTBED_RUNS"]) if os.environ.get("TESTBED_RUNS") else None
COPIES = Path(os.environ.get("TESTBED_COPIES", "/tmp/testbed-copies")) / "test-a2"
MODEL = "opus"  # the Auditor's model; test-a3.py sets another Claude model by the try's name
WORKERS = 3  # Auditor calls at once
CASES = {  # case: (subfolder, input, fixed -var pairs of the original run)
    "density-base": ("density", "density.in", {}), "density-push": ("density", "density.in", {"binw": "1.0"}),
    "slip-base": ("slip", "slip.in", {}), "slip-push": ("slip", "slip.in", {"eps_wf": "0.6"}),
    "viscosity-base": ("viscosity", "viscosity.in", {}), "viscosity-push": ("viscosity", "viscosity.in", {"vwall": "3.0"}),
    "conductance-base": ("conductance", "conductance.in", {}),
    "conductance-push": ("conductance", "conductance.in", {"nequil": "10000"}),
    "pore-base": ("poiseuille", "poiseuille.in", {}), "pore-push": ("poiseuille", "poiseuille.in", {"width": "4"}),
    "slab-base": (".", "liquid_vapour.in", {"localstress": "1"}),
    "slab-hot": (".", "liquid_vapour.in", {"localstress": "1", "T": "1.5"}),
}
HINT = re.compile(r"(?i)(\bpush\b|push it|until it breaks|narrow|knob|break)")
LEAK = re.compile(r"(?i)(test-a|\brep-|[a-z]+-(base|push|hot)\b|\bpush\b|until it breaks|-s(11|22|33)\b)")


def frozen_ok():
    root = HERE / "auditor"
    for line in (root / "SHA256SUMS").read_text().splitlines():
        digest, name = line.split()
        if hashlib.sha256((root / name).read_bytes()).hexdigest() != digest:
            sys.exit(f"frozen file changed: auditor/{name}: stop")


def ids():
    return [line.split() for line in IDS.read_text().splitlines() if line.strip()]


def case_of(label):
    return label.split("-", 1)[1].rsplit("-s", 1)[0], label.rsplit("-s", 1)[1]


def run_folder(label, case):
    sub = CASES[case][0]
    if RUNS is not None:
        return RUNS / label / sub
    if not label.endswith("-s11"):
        sys.exit(f"{label}: only the seed-11 runs are shipped (cases/); set TESTBED_RUNS to a folder of "
                 f"rep-<case>-s<seed>/ runs made with tools/run-case.sh: stop")
    return HERE / "cases" / case / sub


def dehint(text):
    out = []
    for line in text.splitlines():
        code, hash_, comment = line.partition("#")
        if hash_ and HINT.search(comment):
            if code.strip():
                out.append(code.rstrip())
            continue
        out.append(line)
    return "\n".join(out) + "\n"


def index_defaults(folder, inp):
    values = {}
    for f in (folder.parent / "shared_setup.lmp", folder / "shared_setup.lmp", folder / inp):
        if f.exists():
            for m in re.finditer(r"^variable\s+(\w+)\s+index\s+(\S+)", f.read_text(), re.M):
                values.setdefault(m.group(1), m.group(2)) if f.name == "shared_setup.lmp" else values.update({m.group(1): m.group(2)})
    return values


def command(case, seed, extra=None):
    pairs = dict(CASES[case][2], seed=seed, **(extra or {}))
    return f"mpirun -np 8 lmp_mpi -in {CASES[case][1]} " + " ".join(f"-var {k} {v}" for k, v in pairs.items())


def make_copy(src, dest, case, seed, extra=None):
    """The blinded copy the Auditor reads: input, log, shared setup (teaching hints removed), the command line, the
    analysis output, figures, profiles and data. No analysis scripts, no case names."""
    dest.mkdir(parents=True, exist_ok=True)
    inp = CASES[case][1]
    for f in [src / inp, src / "log.lammps", src.parent / "shared_setup.lmp", src / "shared_setup.lmp"]:
        if f.exists():
            (dest / f.name).write_text(dehint(f.read_text(errors="replace")))
    (dest / "command.txt").write_text(command(case, seed, extra) + "\n")
    shutil.copy(src / "analysis.out", dest)
    for f in src.iterdir():
        if f.suffix in (".png", ".profile", ".dat") or f.name.endswith("params.txt"):
            shutil.copy(f, dest)
    for f in dest.rglob("*"):
        if f.is_file() and f.suffix != ".png" and LEAK.search(f.read_text(errors="replace")):
            sys.exit(f"a hint survived in {f}: stop")


def agent(folder, brief, out):
    """One Auditor call: Claude Code, headless, read-only tools (Read, Glob, Grep), no user or project settings."""
    out.parent.mkdir(parents=True, exist_ok=True)
    flags = ["--print", "--no-session-persistence", "--safe-mode", "--restricted", "--tools", "Read,Glob,Grep",
             "--permission-mode", "default", "--permission-prompts", "none", "--max-budget-usd", "5",
             "--model", MODEL, "--output-format", "stream-json", "--verbose"]  # stream-json: every tool call kept
    res = subprocess.run(["claude", *flags, brief], cwd=folder, capture_output=True, text=True, stdin=subprocess.DEVNULL)
    (out.with_suffix(".stream.jsonl")).write_text(res.stdout)
    final = {}
    for line in res.stdout.splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if isinstance(event, dict) and event.get("type") == "result":
            final = event
    (out.with_suffix(".json")).write_text(json.dumps(final))  # the result event = what --output-format json printed
    answer = final.get("result", "") or ""
    out.write_text(answer.strip() + "\n")
    return answer


def field(text, name):
    m = re.search(rf"^{name}:\s*(.*)$", text, re.M)
    return m.group(1).strip() if m else ""


def purpose(case):
    return re.search(rf"^{case}: (.*)$", (T2 / "purposes.md").read_text(), re.M).group(1)


def purpose_block(case):
    text = purpose(case)
    return f"\n## The run's purpose\n{text}\n" if text else ""


def audit1():
    def one(item):
        aid, label = item
        case, seed = case_of(label)
        work = COPIES / aid
        shutil.rmtree(work, ignore_errors=True)
        make_copy(run_folder(label, case), work, case, seed)
        brief = (T2 / "brief-auditor.md").read_text() + purpose_block(case)
        answer = agent(work, brief, T2 / "agents" / aid / "audit1.md")
        return f"{aid}: {field(answer, 'verdict')} | run: {field(answer, 'run')}"
    with cf.ThreadPoolExecutor(WORKERS) as pool:
        for line in pool.map(one, ids()):
            print(line, flush=True)


def steps(values):
    return float(values.get("nequil", 0)) + float(values.get("nprod", 0))


def named_changes(answer):
    """The run an answer names, as {NAME: VALUE}. NAME=OLD→NEW and NAME=OLD→NAME=NEW are read as NAME=NEW (an answer
    that writes `binw=1.0→binw=0.1` would otherwise reach LAMMPS as the value `1.0→binw=0.1`)."""
    named = re.sub(r"(\w+)=[^\s=]*→\1=", r"\1=", field(answer, "run"))
    named = re.sub(r"=[^\s=]*→", "=", named)
    return dict(p.split("=", 1) for p in named.replace(",", " ").split() if "=" in p)


def runs():
    lines, report = [], []
    for aid, label in ids():
        answer = (T2 / "agents" / aid / "audit1.md").read_text()
        named = field(answer, "run")
        if not named or named.lower() == "none":
            continue
        case, seed = case_of(label)
        src = run_folder(label, case)
        defaults = index_defaults(src, CASES[case][1])
        changes = named_changes(answer)
        bad = [k for k in changes if k not in defaults]
        malformed = [f"{k}={v}" for k, v in changes.items() if not re.fullmatch(r"[\w.+-]+", v)]
        before = dict(defaults, **CASES[case][2])
        after = dict(before, **changes)
        if " ".join(f"{k}={v}" for k, v in changes.items()) != named.replace(",", " ").strip():
            named += " (read as " + " ".join(f"{k}={v}" for k, v in changes.items()) + ")"
        if bad:
            report.append(f"{aid}: refused, not index variables: {bad}")
        elif malformed:
            report.append(f"{aid}: refused, value not a plain number or word: {malformed}")
        elif steps(after) > 4 * steps(before):
            report.append(f"{aid}: refused, {steps(after):.0f} steps > 4 x {steps(before):.0f}")
        else:
            pairs = dict(seed=seed)
            pairs.update(changes)  # a seed the Auditor names replaces the run's own
            lines.append(f"{aid}-run {case} " + " ".join(f"{k}={v}" for k, v in pairs.items()))
            report.append(f"{aid}: {named} ({steps(after) - 0:.0f} steps; original {steps(before):.0f})")
    (T1 / "reruns.txt").write_text("\n".join(lines) + "\n")
    (T2 / "runs-checked.txt").write_text("\n".join(report) + "\n")
    print("\n".join(report))


def audit2():
    def one(item):
        aid, label = item
        new = T1 / "reruns" / f"{aid}-run"
        if not new.exists():
            return None
        case, seed = case_of(label)
        first = (T2 / "agents" / aid / "audit1.md").read_text()
        changes = named_changes(first)
        work = COPIES / f"{aid}-2"
        shutil.rmtree(work, ignore_errors=True)
        make_copy(run_folder(label, case), work / "original", case, seed)
        make_copy(new / CASES[case][0], work / "new", case, changes.pop("seed", seed), changes)
        brief = ((T2 / "brief-auditor-followup.md").read_text() + purpose_block(case)
                 + f"\n## The earlier audit\n{first}")
        answer = agent(work, brief, T2 / "agents" / aid / "audit2.md")
        return f"{aid}: {field(answer, 'verdict')} | use: {field(answer, 'use')}"
    with cf.ThreadPoolExecutor(WORKERS) as pool:
        for line in pool.map(one, ids()):
            if line:
                print(line, flush=True)


if __name__ == "__main__":
    frozen_ok()
    print("frozen briefs unchanged (auditor/SHA256SUMS). This file is the driver library; run tools/test-a3.py "
          "(or tools/run-try.sh for a whole try).")
