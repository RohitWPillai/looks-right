#!/usr/bin/env python3
# What: the Auditor loop of Exp 1 on the 12 seed-11 runs (through the driver in tools/test-a2.py), and the outcome
#   score written as code. Cleaned copy of the driver used in the experiments: only the paths changed (relative to this
#   repository), `score` takes --out, and the parts used only by experiments not released here are left out. The
#   outcome rule (outcome, fixed, score_one) is unchanged.
# Who runs it, from the repository root:
#   python3 tools/test-a3.py audit1 <try> [run ids] | runs <try>... | audit2 <try> [run ids]
#   python3 tools/test-a3.py score [original] [--out DIR]           (the released experiment, Exp 1)
#   python3 tools/test-a3.py score [original] --tries T... --out DIR (new tries in TESTBED_RESULTS; no history)
#   (run ids: redo those calls alone, for a call that did not end normally; `runs` writes results/reruns.txt for
#   tools/run-named-runs.sh, which runs them and writes results/reruns/<try>-<id>-run/).
# Refuses: to start if a try's frozen briefs changed (results/test-a3/FROZEN.sha256); the rest as tools/test-a2.py.
import hashlib
import importlib.util
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("a2", HERE / "tools" / "test-a2.py")
a2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a2)
T3 = a2.T1 / "test-a3"  # the results folder's tries (TESTBED_RESULTS, default results/)
A2_IDS = a2.ids  # the original, before setup() points a2.ids at the seed-11 subset
_spec = importlib.util.spec_from_file_location("experiments", HERE / "tools" / "experiments.py")
experiments = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(experiments)
REPEATS = experiments.full_twelve()  # the released experiment's tries (tools/experiments.py)
MODELS = {"haiku": "haiku", "sonnet": "sonnet"}  # try-name prefix -> Claude model for the Auditor; opus for any other try
ORIGINAL_KEY = False  # True: score viscosity-base with the key as fixed before 9 Oct (trusted); `score original`


def frozen_ok():
    if not (T3 / "FROZEN.sha256").exists():  # a fresh results folder before its first try: nothing frozen yet
        return
    for line in (T3 / "FROZEN.sha256").read_text().splitlines():
        digest, name = line.split()
        if hashlib.sha256((T3 / name).read_bytes()).hexdigest() != digest:
            sys.exit(f"frozen file changed: {name}: stop")


def ids():
    return [(aid, lab) for aid, lab in A2_IDS() if lab.endswith("-s11")]


def verdict(text):
    """The answer's verdict, or "" when it has none of the three (an answer without the format is no answer).
    The line is found as the drivers always found it, `verdict: ` at a line's start; in the value, case and marks
    (* _ `) or a full stop around the word are forgiven."""
    v = a2.field(text, "verdict").strip("*_`. ").lower()
    return v if v in ("trusted", "untrusted", "unresolved") else ""


def setup(variant, only=()):
    """Point the driver at this try's folder and rules; `only`: these run ids alone (a call redone)."""
    a2.T2 = T3 / variant
    a2.ids = (lambda: [(aid, lab) for aid, lab in ids() if aid in only]) if only else ids
    a2.MODEL = next((m for prefix, m in MODELS.items() if variant.startswith(prefix)), "opus")
    a2.COPIES = Path(os.environ.get("TESTBED_COPIES", "/tmp/testbed-copies")) / variant


def audit1(variant, only=()):
    setup(variant, only)
    a2.audit1()


def runs(variants):
    lines = []
    for v in variants:
        setup(v)
        a2.runs()
        silent = {aid for aid, _ in ids() if not verdict((a2.T2 / "agents" / aid / "audit1.md").read_text())}
        if silent:  # an answer without a verdict names no run
            checked = a2.T2 / "runs-checked.txt"
            checked.write_text("".join(f"{line.split(':')[0]}: refused, no verdict\n" if line.split(":")[0] in silent
                                       else line + "\n" for line in checked.read_text().splitlines()))
        lines += [f"{v}-{line}" for line in (a2.T1 / "reruns.txt").read_text().splitlines()
                  if line.strip() and line.split("-run")[0] not in silent]
    (a2.T1 / "reruns.txt").write_text("\n".join(lines) + "\n")
    print(f"{len(lines)} named runs listed")


def audit2(variant, only=()):
    setup(variant, only)
    real = a2.T1

    class Shim:  # Test A2's audit2 looks for T1/reruns/<id>-run; here the runs are <variant>-<id>-run
        def __truediv__(self, name):
            return real / name if name != "reruns" else RerunsShim()

    class RerunsShim:
        def __truediv__(self, name):
            return real / "reruns" / (f"{variant}-{name}" if name.endswith("-run") else name)
    a2.T1 = Shim()
    try:
        a2.audit2()
    finally:
        a2.T1 = real


# The outcome rule, as applied by hand to Test A2 (7 Oct), written before Test A3 ran.
def number(folder, case):
    fam = case.split("-")[0]
    text = (folder / "analysis.out").read_text(errors="replace") if (folder / "analysis.out").exists() else ""
    pats = {"density": r"layering contrast ([\d.]+)x", "conductance": r"imbalance ([\d.]+)%"}
    m = re.search(pats.get(fam, r"$^"), text)
    temps = re.search(r"walls ~([\d.]+) / ([\d.]+), centre ~([\d.]+)", text)
    return (float(m.group(1)) if m else None), temps


def outcome(case, final, use, named, new_folder):
    if case == "slip-push":
        return "unknown"
    if case == "slab-hot":
        return "right" if final != "trusted" and not re.search(r"\bT=", named) else "wrong acceptance"
    if case == "pore-push":
        return "wrong acceptance" if final == "trusted" else "right"
    if case == "viscosity-base" and not ORIGINAL_KEY:  # key corrected 9 Oct: the input leaves out the kinetic stress
        return "right" if final != "trusted" else "wrong acceptance"
    if case == "slip-base":
        return "wrong acceptance" if final == "trusted" and use != "new" else "right"
    if case.endswith("-base"):
        return "right" if final == "trusted" else "too strict"
    # density-push, viscosity-push, conductance-push: right only if the trusted measurement is the fixed new run
    if final != "trusted":
        return "too strict" if new_folder and fixed(case, new_folder) else "missed fix"
    if use != "new" or not new_folder:
        return "wrong acceptance"
    return "right" if fixed(case, new_folder) else "wrong acceptance"


def fixed(case, folder):
    value, temps = number(folder, case)
    if case == "density-push":
        return value is not None and value >= 1.5
    if case == "conductance-push":
        return value is not None and value < 5
    if case == "viscosity-push":
        return temps is not None and max(map(float, temps.groups())) < 1.2
    return False


def score_one(root, run_name, variant_ids):
    tally, rows, causes = {}, [], []
    for aid, label in variant_ids:
        case = a2.case_of(label)[0]
        a1 = (root / "agents" / aid / "audit1.md").read_text()
        p2 = root / "agents" / aid / "audit2.md"
        final = verdict(p2.read_text()) if p2.exists() else verdict(a1)
        use = a2.field(p2.read_text(), "use") if p2.exists() else "original"
        named = a2.field(a1, "run")
        new = a2.T1 / "reruns" / run_name(aid) / a2.CASES[case][0]
        result = outcome(case, final, use, named, new if new.exists() else None)
        if result != "unknown" and not final:  # an answer without a verdict is no answer (a first look without
            result = "no answer"  # one names no run, so it has no second look)
        if case == "pore-push" and result == "right":  # rule of 8 Oct: right only if the cause is the layering
            cause = a2.field(p2.read_text(), "cause") if p2.exists() else a2.field(a1, "cause")
            causes.append(f"- {aid} ({final}): {cause}")
        tally[result] = tally.get(result, 0) + 1
        steps = re.search(rf"^{aid}: .*\((\d+) steps", (root / "runs-checked.txt").read_text(), re.M) \
            if (root / "runs-checked.txt").exists() else None
        tally["steps named"] = tally.get("steps named", 0) + (int(steps.group(1)) if steps else 0)
        tally["runs named"] = tally.get("runs named", 0) + (1 if steps else 0)
        rows.append(f"| {aid} | {case} | {a2.field(a1, 'verdict')} | {named} | {final} / {use} | {result} |")
    if causes:
        rows.append("\npore-push answers scored right by the outcome rule; each counts only if its cause is the "
                    "layering, else right answer, wrong reason (read by hand):\n" + "\n".join(causes))
    return tally, rows


def score(out_dir=None, tries=None):
    """Every released try that has looks; or, with `tries`, only those (new tries, in TESTBED_RESULTS)."""
    out = ["# Test A3: one change at a time (seed 11, 12 cases each)\n",
           "Outcome rule: `tools/test-a3.py` (outcome), written before Test A3 ran.\n"]
    a2ids = ids()
    totals = {}
    for v in (tries or sum(REPEATS.values(), [])):
        if not (T3 / v / "agents").exists():
            continue
        tally, rows = score_one(T3 / v, lambda aid, v=v: f"{v}-{aid}-run", a2ids)
        totals[v] = tally.get("right", 0)
        out.append(f"## {v}\n{tally}\n\n| id | case | first | named run | final / use | outcome |\n|---|---|---|---|---|---|\n"
                   + "\n".join(rows) + "\n")
    for name, names in ({"new tries": tries} if tries else REPEATS).items():
        rep = [totals[v] for v in names if v in totals]
        if rep:
            out.append(f"## {name} summary\nright per try (before the pore-push cause reading): {rep}; "
                       f"spread {max(rep) - min(rep)}\n")
    dest = Path(out_dir) if out_dir else HERE / "results"
    dest.mkdir(parents=True, exist_ok=True)
    (dest / ("SCORE-original-key.md" if ORIGINAL_KEY else "SCORE.md")).write_text("\n".join(out))
    print("\n".join(out))


if __name__ == "__main__":
    frozen_ok()
    cmd = sys.argv[1]
    out_dir = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None
    if cmd == "score":
        ORIGINAL_KEY = "original" in sys.argv[2:]
        new = []
        if "--tries" in sys.argv:
            new = [a for a in sys.argv[sys.argv.index("--tries") + 1:] if not a.startswith("--")]
            new = new[:new.index(out_dir)] if out_dir in new else new
            if not out_dir:
                sys.exit("score --tries needs --out DIR (the released results/ stay as shipped): stop")
        score(out_dir, new)
    elif a2.T1 == HERE / "results":
        sys.exit("audit1, runs and audit2 write answers: set TESTBED_RESULTS to a new results folder (the released "
                 "results/ stay as shipped): stop")
    elif cmd == "runs":
        runs(sys.argv[2:])
    else:
        {"audit1": audit1, "audit2": audit2}[cmd](sys.argv[2], sys.argv[3:])
