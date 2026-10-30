"""Tests of the score tables in tools/tables.py: Exp 1's right answers per try under both keys, the view without the
disputed narrow-pore run (pore-push), and the accept-everything baseline. Hermetic: the shipped score files are read,
the tables are written to a temporary folder only.
Run from the repository root:  python3 -m pytest -q tests"""
import csv
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), ROOT / "tools" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def tables_in(tmp_path):
    tables = load("tables")
    tables.main(ROOT / "results", tmp_path)
    with open(tmp_path / "right-per-try.csv") as f:
        return tables, list(csv.DictReader(f)), (tmp_path / "SUMMARY.md").read_text()


def test_the_view_without_pore_push_is_the_11_run_count_less_that_case(tmp_path):
    tables, rows, _ = tables_in(tmp_path)
    cor, excl = tables.sections(ROOT / "results" / "SCORE.md"), tables.not_counted()
    for r in rows:
        t = r["try"]
        pore = tables.right(t, "pore-push", cor[t]["pore-push"], excl)
        assert int(r["right_of_10_without_pore_push"]) == int(r["right_of_11_corrected_key"]) - pore


def test_exp1_numbers_and_the_baseline(tmp_path):
    _, rows, md = tables_in(tmp_path)
    assert {r["experiment"] for r in rows} == {"Exp 1 (Opus, base)"}
    assert [int(r["right_of_11_corrected_key"]) for r in rows] == [9, 9, 8, 10, 10, 9, 10, 9, 9, 10]
    assert [int(r["right_of_11_original_key"]) for r in rows] == [10, 8, 9, 9, 9, 8, 9, 10, 10, 9]
    assert ("| Exp 1 (Opus, base) | 10 | 9, 9, 8, 10, 10, 9, 10, 9, 9, 10 | 9.3 | 10, 8, 9, 9, 9, 8, 9, 10, 10, 9 | "
            "9.1 |") in md
    assert "right on 4 of 11 (corrected key), 5 of 11 (original key); without pore-push, 4 of 10." in md
