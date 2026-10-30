#!/usr/bin/env python3
# What: what each Auditor call looked at and how its verdicts vary, per try of the test bed: files opened and searched
#   (from each call's stream, results/test-a3/<try>/agents/<id>/audit1|2.stream.jsonl, kept from Exp 1 try 6 on; in this
#   repository each stream is reduced to its tool calls, with paths made relative to the run copy, "copy/") and, per case, the
#   first and final verdict of every try (from audit1.md / audit2.md, every try). Tokens: tools/token-usage.py.
# Who runs it, from the repository root:  python3 tools/call-measures.py <try> ... [--by-case]
# Refuses: nothing; a call with no stream is left out of the file counts and said so.
import json
import re
import sys
from pathlib import Path

T3 = Path(__file__).resolve().parent.parent / "results" / "test-a3"
CASES = dict(re.findall(r"^\| (A\d\d) \| ([a-z]+-[a-z]+) \|", (T3.parent / "SCORE.md").read_text(), re.M))  # id -> case
KINDS = ["log", "analysis", "figure", "input", "command", "data"]


def kind(name):
    if name == "log.lammps":
        return "log"
    if name == "analysis.out":
        return "analysis"
    if name == "command.txt":
        return "command"
    if name.endswith(".png"):
        return "figure"
    if name.endswith((".in", ".lmp")) or "params" in name:
        return "input"
    return "data"


def looked_at(stream):
    """Reads, searches and the set of files a call touched (a search with no path counts as all files)."""
    reads = searches = 0
    files = set()
    cwd = ""
    for line in stream.read_text().splitlines():
        try:
            e = json.loads(line)
        except ValueError:
            continue
        if e.get("type") == "system" and e.get("subtype") == "init":
            cwd = e.get("cwd", "").rstrip("/") + "/"
        if e.get("type") != "assistant":
            continue
        for c in e.get("message", {}).get("content", []):
            if c.get("type") != "tool_use":
                continue
            inp = c.get("input", {})
            if c["name"] == "Read":
                reads += 1
                files.add(inp.get("file_path", "").replace(cwd, ""))
            elif c["name"] in ("Grep", "Glob"):
                searches += 1
                if c["name"] == "Grep" and inp.get("path") and Path(inp["path"].replace(cwd, "")).suffix:  # a file, not the folder (the original asked the disk; the copies are gone)
                    files.add(inp["path"].replace(cwd, ""))
    return reads, searches, files


def file_table(tries, by_case):
    print("| try | calls with a stream | without | reads per call | searches per call | distinct files per call | "
          + " | ".join(f"opened {k}" for k in KINDS) + " |\n|" + "---|" * (6 + len(KINDS)))
    per_case = {}
    for t in tries:
        rows, missing = [], 0
        for md in sorted((T3 / t / "agents").glob("*/audit*.md")):
            s = md.with_suffix(".stream.jsonl")
            if not s.exists():
                missing += 1
                continue
            r, q, f = looked_at(s)
            kinds = {kind(Path(x).name) for x in f}
            rows.append((r, q, len(f), kinds))
            per_case.setdefault(md.parent.name, []).append((r, len(f), kinds))
        n = len(rows)
        if not n:
            print(f"| {t} | 0 | {missing} |" + " - |" * (3 + len(KINDS)))
            continue
        share = [f"{sum(k in x[3] for x in rows) / n:.0%}" for k in KINDS]
        print(f"| {t} | {n} | {missing} | {sum(x[0] for x in rows) / n:.1f} | {sum(x[1] for x in rows) / n:.1f} | "
              f"{sum(x[2] for x in rows) / n:.1f} | " + " | ".join(share) + " |")
    if by_case and per_case:
        print("\nBy case, over these tries (both looks):\n| case | calls | reads per call | distinct files per call | "
              "opened log | opened a figure |\n|---|---|---|---|---|---|")
        for aid in sorted(per_case):
            v = per_case[aid]
            print(f"| {aid} {CASES.get(aid, '')} | {len(v)} | {sum(x[0] for x in v) / len(v):.1f} | "
                  f"{sum(x[1] for x in v) / len(v):.1f} | {sum('log' in x[2] for x in v)}/{len(v)} | "
                  f"{sum('figure' in x[2] for x in v)}/{len(v)} |")


def verdict(path):
    m = re.search(r"^verdict:\s*(\w+)", path.read_text(), re.M) if path.exists() else None
    return {"trusted": "T", "untrusted": "U", "unresolved": "R"}.get(m.group(1).lower(), "?") if m else "-"


def verdict_table(tries):
    print(f"\nVerdicts per case, one letter per try ({', '.join(tries)}); T trusted, U untrusted, R unresolved, "
          "- no second look:\n| case | first look | second look | final |\n|---|---|---|---|")
    for aid in sorted(CASES):
        first = [verdict(T3 / t / "agents" / aid / "audit1.md") for t in tries]
        second = [verdict(T3 / t / "agents" / aid / "audit2.md") for t in tries]
        final = [b if b != "-" else a for a, b in zip(first, second)]
        print(f"| {aid} {CASES[aid]} | {' '.join(first)} | {' '.join(second)} | {' '.join(final)} |")


if __name__ == "__main__":
    tries = [a for a in sys.argv[1:] if not a.startswith("--")]
    file_table(tries, "--by-case" in sys.argv)
    verdict_table(tries)
