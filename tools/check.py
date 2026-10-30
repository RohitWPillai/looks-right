#!/usr/bin/env python3
# What: regenerates every results table from the shipped verdict files and checks it against results/ (and, where the
#   experiments kept one, against the file as recorded at the time, results/as-recorded/). No model calls, no LAMMPS.
# Who runs it, from the repository root:  python3 tools/check.py          (exit 0: everything matches)
#                                         python3 tools/check.py --write  (rewrite results/ from the regenerated files)
# Needs: Python 3.10 or later, numpy, matplotlib (the pore scan's figure).
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RES = ROOT / "results"
REC = RES / "as-recorded"
TRIES = [f"exp1r{r}" for r in range(1, 11)]  # Exp 1, the released experiment
STREAMS = [f"exp1r{r}" for r in range(6, 11)]  # the tries whose calls kept a stream


def run(args, out=None):
    res = subprocess.run([sys.executable, *args], cwd=ROOT, capture_output=True, text=True)
    if res.returncode != 0:
        sys.exit(f"failed: {' '.join(args)}\n{res.stderr}")
    if out:
        out.write_text(res.stdout)
    return res.stdout


def main(write):
    tmp = Path(tempfile.mkdtemp(prefix="testbed-check-"))
    run(["tools/test-a3.py", "score", "--out", str(tmp)])
    run(["tools/test-a3.py", "score", "original", "--out", str(tmp)])
    run(["tools/tables.py", "--scores", str(tmp), "--out", str(tmp)])
    run(["tools/token-usage.py", *TRIES], tmp / "tokens.md")
    run(["tools/token-usage.py", *TRIES, "--cases"], tmp / "tokens-by-case.md")
    run(["tools/call-measures.py", *STREAMS, "--by-case"], tmp / "files-opened.md")
    run(["key-checks/viscosity-kinetic/summarise.py"], tmp / "viscosity-kinetic-SUMMARY.md")
    run(["key-checks/pore-scan/scan-b.py", "--out", str(tmp / "scan")])

    generated = ["SCORE.md", "SCORE-original-key.md", "SUMMARY.md", "right-per-try.csv", "right-per-case.csv",
                 "tokens.md", "tokens-by-case.md", "files-opened.md"]
    if write:
        for name in generated:
            shutil.copyfile(tmp / name, RES / name)
    fails = []

    def same(a, b, label):
        ok = a.read_text().splitlines() == b.read_text().splitlines()
        print(f"{'match' if ok else 'DIFFER'}: {label}")
        if not ok:
            fails.append(label)

    for name in generated:
        same(tmp / name, RES / name, f"results/{name} regenerated")
    # against the files the experiments wrote at the time (as-recorded/ keeps their Exp 1 sections)
    same(tmp / "SCORE.md", REC / "SCORE.md", "SCORE.md against the experiments' own (Exp 1 tries)")
    mine = dict(s.split("\n", 1) for s in (tmp / "SCORE-original-key.md").read_text().split("\n## ")[1:])
    theirs = dict(s.split("\n", 1) for s in (REC / "SCORE-original-key.md").read_text().split("\n## ")[1:])
    diff = [k for k in theirs if mine.get(k, "").strip() != theirs[k].strip()]
    print(f"{'match' if not diff else 'DIFFER'}: SCORE-original-key.md against the experiments' own, every section "
          f"it has ({len(theirs)} sections)")
    if diff:
        fails.append(f"original-key sections {diff}")
    # the view without pore-push equals the 11-run count less that case's outcome, read from the regenerated SCORE.md
    import csv
    import importlib.util
    spec = importlib.util.spec_from_file_location("tables", ROOT / "tools" / "tables.py")
    T = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(T)
    cor, excl = T.sections(tmp / "SCORE.md"), T.not_counted()
    with open(tmp / "right-per-try.csv") as f:
        bad = [(r["try"], col) for r in csv.DictReader(f) for col, case in T.VIEWS.items()
               if int(r[col]) != int(r["right_of_11_corrected_key"]) - T.right(r["try"], case, cor[r["try"]][case],
                                                                               excl)]
    print(f"{'match' if not bad else 'DIFFER'}: without-pore-push view against the 11-run counts")
    if bad:
        fails.append(f"views {bad}")
    same(tmp / "viscosity-kinetic-SUMMARY.md", ROOT / "key-checks" / "viscosity-kinetic" / "SUMMARY.md",
         "viscosity kinetic-stress check SUMMARY.md")
    same(tmp / "scan" / "RESULT.md", ROOT / "key-checks" / "pore-scan" / "RESULT.md", "pore scan RESULT.md")
    shutil.rmtree(tmp)
    if fails:
        sys.exit(f"{len(fails)} differ: {fails}")
    print("all tables regenerate and match")


if __name__ == "__main__":
    main("--write" in sys.argv)
