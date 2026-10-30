"""Tests of the release's tools. Hermetic: temporary folders only, a stand-in LAMMPS and Python, no model calls.
Run from the repository root:  python3 -m pytest -q tests"""
import importlib.util
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), ROOT / "tools" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def stub(path, body):
    path.write_text("#!/bin/bash\n" + body)
    path.chmod(0o755)


def fake_tools(tmp):
    """A stand-in mpirun (runs its program), LAMMPS (writes a log) and Python (writes a line of analysis)."""
    bin_ = tmp / "bin"
    bin_.mkdir()
    stub(bin_ / "mpirun", 'shift 2; exec "$@"\n')
    stub(bin_ / "lmp", 'echo "LAMMPS stand-in $*" > log.lammps; echo ran\n')
    stub(bin_ / "py", 'echo "analysis of $1"\n')
    return {**os.environ, "MPIRUN": str(bin_ / "mpirun"), "LMP": str(bin_ / "lmp"), "PYTHON": str(bin_ / "py"),
            "NP": "1"}


def test_run_case_relative_output_keeps_the_course_layout(tmp_path):
    env = fake_tools(tmp_path)
    work = tmp_path / "here"
    work.mkdir()
    res = subprocess.run(["bash", str(ROOT / "tools" / "run-case.sh"), "pore-push", "out", "seed=11"], cwd=work,
                         env=env, capture_output=True, text=True)
    assert res.returncode == 0, res.stderr
    out = work / "out"
    assert (out / "shared_setup.lmp").exists() and (out / "lammps_io.py").exists()
    assert (out / "poiseuille" / "poiseuille.in").exists()
    assert "-var width 4" in (out / "poiseuille" / "log.lammps").read_text()
    assert "-var seed 11" in (out / "poiseuille" / "log.lammps").read_text()
    assert "analysis of analyse_poiseuille.py" in (out / "poiseuille" / "analysis.out").read_text()


def test_run_case_refuses_a_name_that_is_not_an_index_variable(tmp_path):
    env = fake_tools(tmp_path)
    res = subprocess.run(["bash", str(ROOT / "tools" / "run-case.sh"), "density-base", str(tmp_path / "o"),
                          "nosuchvar=1"], env=env, capture_output=True, text=True)
    assert res.returncode != 0 and "not an index variable" in res.stderr


def test_one_shared_experiment_list():
    exps = load("experiments")
    a3 = load("test-a3")
    tables = load("tables")
    assert a3.REPEATS == {name: tries for name, (_, tries) in exps.HISTORICAL.items()}
    assert [t for tries in tables.ARMS.values() for t in tries] == \
        [t for _, tries in exps.HISTORICAL.values() for t in tries]
    assert list(exps.HISTORICAL) == ["Exp 1"] and exps.HISTORICAL["Exp 1"][1] == [f"exp1r{r}" for r in range(1, 11)]


def test_a_new_try_is_scored_in_its_own_folder_and_history_is_untouched(tmp_path):
    before = (ROOT / "results" / "SCORE.md").read_bytes()
    new = tmp_path / "new-results"
    (new / "test-a3").mkdir(parents=True)
    shutil.copytree(ROOT / "results" / "test-a3" / "exp1r1", new / "test-a3" / "exp1r91")
    for d in (ROOT / "results" / "reruns").glob("exp1r1-*"):
        shutil.copytree(d, new / "reruns" / d.name.replace("exp1r1-", "exp1r91-"))
    lines = [l.replace("exp1r1/", "exp1r91/") for l in
             (ROOT / "results" / "test-a3" / "FROZEN.sha256").read_text().splitlines() if " exp1r1/" in l]
    (new / "test-a3" / "FROZEN.sha256").write_text("\n".join(lines) + "\n")
    env = {**os.environ, "TESTBED_RESULTS": str(new)}
    res = subprocess.run([sys.executable, "tools/test-a3.py", "score", "--tries", "exp1r91", "--out", str(new)],
                         cwd=ROOT, env=env, capture_output=True, text=True)
    assert res.returncode == 0, res.stderr
    mine = (new / "SCORE.md").read_text().split("## exp1r91\n")[1].split("\n## ")[0]
    theirs = before.decode().split("## exp1r1\n")[1].split("\n## ")[0]
    assert mine.strip() == theirs.strip()
    assert (ROOT / "results" / "SCORE.md").read_bytes() == before


def test_the_frozen_briefs_are_unchanged():
    res = subprocess.run([sys.executable, "tools/test-a2.py"], cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0, res.stdout + res.stderr
    listed = [line.split()[1] for line in (ROOT / "auditor" / "SHA256SUMS").read_text().splitlines()]
    assert sorted(listed) == sorted(f"exp1-frozen/{p.name}" for p in (ROOT / "auditor" / "exp1-frozen").iterdir())


def test_run_try_refuses_to_write_into_the_released_results(tmp_path):
    bin_ = tmp_path / "bin"  # a stand-in claude and codex first on the PATH: no model can be called by this test
    bin_.mkdir()
    for name in ("claude", "codex", "mpirun", "lmp_mpi"):
        stub(bin_ / name, "echo stand-in; exit 1\n")
    env = {**os.environ, "PATH": f"{bin_}:{os.environ['PATH']}", "TESTBED_RESULTS": str(ROOT / "results")}
    res = subprocess.run(["bash", "tools/run-try.sh", "exp1r92"], cwd=ROOT, env=env, capture_output=True, text=True)
    assert res.returncode != 0 and "released results" in res.stderr
    assert not (ROOT / "results" / "test-a3" / "exp1r92").exists()
