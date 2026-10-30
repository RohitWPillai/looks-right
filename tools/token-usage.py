#!/usr/bin/env python3
# What: token use of the Auditor calls, per try of the test bed, from the result each call saved next to its answer
#   (results/test-a3/<try>/agents/<id>/audit1.json, audit2.json; in this repository each holds only the result event's
#   usage, cost, turns and duration fields). First and second looks are kept apart: every try has the same 12
#   first looks, while the number of second looks varies. Cost is the list price the CLI reports, a proxy only.
# Who runs it, from the repository root:  python3 tools/token-usage.py [try ...] [--cases]
#   (default: every try; a total row for each experiment with two or more tries listed; --cases: means per case).
# Refuses: nothing. A call counts as missing when its file is absent (an audit1 per case; an audit2 per first look that
#   named a run), unreadable, has no usage block, or reports an error.
import json
import re
import sys
from pathlib import Path

T3 = Path(__file__).resolve().parent.parent / "results" / "test-a3"
KEYS = ("turns", "fresh", "cached", "output", "thinking", "usd", "min")


def usage(f):
    try:
        d = json.loads(f.read_text())
        u = d["usage"]
        if d.get("is_error") or not isinstance(u, dict):
            return None
        return {"turns": d.get("num_turns") or 0,
                "fresh": (u.get("input_tokens") or 0) + (u.get("cache_creation_input_tokens") or 0),
                "cached": u.get("cache_read_input_tokens") or 0,
                "output": u.get("output_tokens") or 0,
                "thinking": (u.get("output_tokens_details") or {}).get("thinking_tokens") or 0,
                "usd": d.get("total_cost_usd") or 0.0, "min": (d.get("duration_ms") or 0) / 60000}
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        return None


def calls(try_name):
    """{look: [(id, usage or None)]} for every call that should exist."""
    out = {"audit1": [], "audit2": []}
    for case in sorted(p for p in (T3 / try_name / "agents").iterdir() if p.is_dir()):
        out["audit1"].append((case.name, usage(case / "audit1.json")))
        first = (case / "audit1.md").read_text() if (case / "audit1.md").exists() else ""
        run = re.search(r"^run:\s*(.*)$", first, re.M)
        if (run and run.group(1).strip().lower() not in ("", "none")) or (case / "audit2.json").exists():
            out["audit2"].append((case.name, usage(case / "audit2.json")))
    return out


def row(name, c):
    a1 = [u for _, u in c["audit1"] if u]
    a2 = [u for _, u in c["audit2"] if u]
    s = {k: sum(u[k] for u in a1 + a2) for k in KEYS}
    n = len(a1) + len(a2)
    per = lambda xs, k: f"{sum(u[k] for u in xs) / len(xs) / 1e3:.2f} k" if xs else "-"
    return (f"| {name} | {len(a1)} | {len(c['audit1']) - len(a1)} | {per(a1, 'output')} | {per(a1, 'thinking')} | "
            f"{len(a2)} | {len(c['audit2']) - len(a2)} | {per(a2, 'output')} | {s['turns'] / max(n, 1):.1f} | "
            f"{s['fresh'] / 1e6:.2f} M | {s['cached'] / 1e6:.2f} M | {s['output'] / 1e3:.1f} k | ${s['usd']:.2f} | "
            f"{s['min']:.0f} |")


def main(args):
    tries = [a for a in args if not a.startswith("--")] or sorted(
        p.name for p in T3.iterdir() if (p / "agents").is_dir())
    print("| try | first looks | missing | output per first look | of which thinking | second looks | missing | "
          "output per second look | turns per call | fresh input | cache reads | output | list cost | call minutes |\n"
          "|" + "---|" * 14)
    groups = {}
    for t in tries:
        c = calls(t)
        print(row(t, c))
        m = re.match(r"(exp\d+)r\d+$", t)
        if m:
            g = groups.setdefault(m.group(1), {"audit1": [], "audit2": [], "n": 0})
            g["audit1"] += c["audit1"]
            g["audit2"] += c["audit2"]
            g["n"] += 1
    for name, g in groups.items():
        if g["n"] >= 2:
            print(row(f"**{name}, {g['n']} tries**", g))
    if "--cases" in args:
        cases = dict(re.findall(r"^\| (A\d\d) \| ([a-z]+-[a-z]+) \|", (T3.parent / "SCORE.md").read_text(), re.M))
        print(f"\nMean output tokens (k) per call, by case and look, over {', '.join(tries)}:\n"
              "| case | first look | second look |\n|---|---|---|")
        per = {}
        for t in tries:
            for look, items in calls(t).items():
                for aid, u in items:
                    if u:
                        per.setdefault((aid, look), []).append(u["output"])
        for aid in sorted({a for a, _ in per}):
            cells = [f"{sum(v) / len(v) / 1e3:.1f} (n={len(v)})" if (v := per.get((aid, lk))) else "-"
                     for lk in ("audit1", "audit2")]
            print(f"| {aid} {cases.get(aid, '')} | {cells[0]} | {cells[1]} |")


if __name__ == "__main__":
    main(sys.argv[1:])
