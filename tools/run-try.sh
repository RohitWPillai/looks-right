#!/bin/bash
# What: one new Auditor try on all 12 cases, end to end, as Exp 1 ran: first looks, the named runs checked,
#   run locally with LAMMPS, second looks, then the try's score. Everything goes in a separate results folder,
#   TESTBED_RESULTS (default new-results/), so the released results/ and tools/check.py stay as shipped.
# Who runs it, from the repository root:  bash tools/run-try.sh <new try name> [frozen brief folder]
#   e.g.  bash tools/run-try.sh exp1r11 auditor/exp1-frozen     (Exp 1's Auditor, an eleventh try)
#   The try's model follows its name's prefix (the prefix table MODELS in tools/test-a3.py; a name matching none
#   runs Opus). Costs money: model calls, 3.80 to 4.71 US dollars per Opus try at list price as measured, plus LAMMPS
#   time for the runs it names (6 to 9 per try as measured).
# Refuses: the released results/ as its results folder; an existing try folder; a first look without a verdict line;
#   a LAMMPS failure.
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT=$PWD
try=${1:?usage: run-try.sh <new try name> [frozen brief folder]}; briefs=${2:-auditor/exp1-frozen}
export TESTBED_RESULTS=${TESTBED_RESULTS:-$ROOT/new-results}
case "$TESTBED_RESULTS" in /*) ;; *) TESTBED_RESULTS="$ROOT/$TESTBED_RESULTS" ;; esac
mkdir -p "$TESTBED_RESULTS/test-a3"
[ "$(cd "$TESTBED_RESULTS" && pwd)" != "$ROOT/results" ] || {
  echo "will not write into the released results/: set TESTBED_RESULTS to a new folder" >&2; exit 1; }
T=$TESTBED_RESULTS/test-a3/$try
[ ! -e "$T" ] || { echo "$T exists: stop" >&2; exit 1; }
mkdir -p "$T"
for f in brief-auditor.md brief-auditor-followup.md purposes.md; do
  cp "$briefs/$f" "$T/$f"
  echo "$(shasum -a 256 "$T/$f" | cut -d' ' -f1)  $try/$f" >> "$TESTBED_RESULTS/test-a3/FROZEN.sha256"
done
python3 tools/test-a3.py audit1 "$try"
bad=$( (grep -L '^verdict: ' "$T"/agents/*/audit1.md || true) | wc -l | tr -d ' ')
[ "$bad" -eq 0 ] || { echo "$bad first looks have no verdict line: stop" >&2; exit 1; }
python3 tools/test-a3.py runs "$try"
bash tools/run-named-runs.sh
python3 tools/test-a3.py audit2 "$try"
python3 tools/test-a3.py score --tries "$try" --out "$TESTBED_RESULTS"
echo "$try: scored in $TESTBED_RESULTS/SCORE.md"
