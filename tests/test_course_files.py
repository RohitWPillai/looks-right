"""The course carve-out list (COURSE-FILES.md) names real files and covers every course-authored source file."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def listed():
    return set(re.findall(r"^- `([^`]+)`", (ROOT / "COURSE-FILES.md").read_text(), re.M))


def test_every_listed_path_exists():
    missing = [p for p in listed() if not (ROOT / p).is_file()]
    assert not missing, missing


def test_every_course_source_file_is_listed():
    names = {"shared_setup.lmp", "lammps_io.py", "intrinsic_surface.py"}
    found = {str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts
             and p.parts[len(ROOT.parts)] in ("cases", "key-checks")
             and (p.name in names or p.suffix == ".in" or (p.name.startswith("analyse_") and p.suffix == ".py"))}
    assert found and found <= listed(), sorted(found - listed())
