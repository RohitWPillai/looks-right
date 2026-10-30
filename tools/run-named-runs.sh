#!/bin/bash
# What: runs every named run listed in <results>/reruns.txt (written by `tools/test-a3.py runs <try>...`), one after
#   another on this machine, into <results>/reruns/<label>/ (the case's layout), where the second look and the scorer
#   find it. <results> is TESTBED_RESULTS (default new-results/; the released results/ are never written).
#   The experiments ran the same commands detached on a Mac mini (8 MPI ranks); this is the local equivalent.
# Who runs it, from the repository root:  bash tools/run-named-runs.sh     (environment as tools/run-case.sh)
# Refuses: to overwrite a run that already exists (it is skipped); stops at the first LAMMPS failure.
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
RES=${TESTBED_RESULTS:-$ROOT/new-results}; case "$RES" in /*) ;; *) RES="$PWD/$RES" ;; esac
[ "$(cd "$RES" 2>/dev/null && pwd)" != "$ROOT/results" ] || { echo "will not write into the released results/: set TESTBED_RESULTS" >&2; exit 1; }
while read -r label name changes; do
  [ -n "${label:-}" ] || continue
  dest="$RES/reruns/$label"
  [ -e "$dest" ] && { echo "$label: exists, skipped"; continue; }
  # shellcheck disable=SC2086  # $changes is a list of NAME=VALUE pairs
  bash "$ROOT/tools/run-case.sh" "$name" "$dest" $changes
done < "$RES/reruns.txt"
echo "all named runs done"
