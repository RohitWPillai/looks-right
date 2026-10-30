#!/bin/bash
# What: reruns one of the 12 cases with LAMMPS and the course's analysis script, as the experiments did: the case's
#   input with its fixed -var settings, the seed, and any NAME=VALUE changes (a named run), then the analysis.
# Who runs it, from the repository root:
#   bash tools/run-case.sh <case> <output folder> [NAME=VALUE ...]      e.g.  bash tools/run-case.sh pore-push /tmp/pp seed=11
#   Environment: NP (MPI ranks, default 8, as used), LMP (LAMMPS binary, default lmp_mpi), MPIRUN (default mpirun),
#   PYTHON (default python3). The output folder must not exist yet. It gets the case's whole folder as in cases/<case>/
#   (for the channel and pore cases: shared_setup.lmp and lammps_io.py at the top, the run in its subfolder), with
#   the new outputs in place of the old.
# Refuses: an unknown case; a NAME that is not an `index` variable of the case's input or the shared setup it includes;
#   an existing output folder. Stops at a LAMMPS failure; a failing analysis is recorded in analysis.out, not a stop.
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
case_name=${1:?usage: run-case.sh <case> <output folder> [NAME=VALUE ...]}; out=${2:?output folder}; shift 2
case "$out" in /*) ;; *) out="$PWD/$out" ;; esac  # resolved before any cd: a relative path means the caller's folder
NP=${NP:-8}; LMP=${LMP:-lmp_mpi}; MPIRUN=${MPIRUN:-mpirun}; PYTHON=${PYTHON:-python3}

# case | subfolder | input | fixed -var arguments of the original run | analysis script
table() { cat <<'T'
density-base|density|density.in||analyse_density.py
density-push|density|density.in|-var binw 1.0|analyse_density.py
slip-base|slip|slip.in||analyse_slip.py
slip-push|slip|slip.in|-var eps_wf 0.6|analyse_slip.py
viscosity-base|viscosity|viscosity.in||analyse_viscosity.py
viscosity-push|viscosity|viscosity.in|-var vwall 3.0|analyse_viscosity.py
conductance-base|conductance|conductance.in||analyse_conductance.py
conductance-push|conductance|conductance.in|-var nequil 10000|analyse_conductance.py
pore-base|poiseuille|poiseuille.in||analyse_poiseuille.py
pore-push|poiseuille|poiseuille.in|-var width 4|analyse_poiseuille.py
slab-base|.|liquid_vapour.in|-var localstress 1|analyse_liquid_vapour.py
slab-hot|.|liquid_vapour.in|-var localstress 1 -var T 1.5|analyse_liquid_vapour.py
T
}
row=$(table | grep "^$case_name|") || { echo "unknown case: $case_name" >&2; exit 1; }
IFS='|' read -r _ sub input vars analysis <<< "$row"
[ ! -e "$out" ] || { echo "$out exists: stop" >&2; exit 1; }
src="$ROOT/cases/$case_name"
args="$vars"
for pair in "$@"; do
  var=${pair%%=*}; val=${pair#*=}
  grep -qE "^variable[[:space:]]+$var[[:space:]]+index" "$src/$sub/$input" "$src/shared_setup.lmp" 2>/dev/null \
    || { echo "$var is not an index variable of $input: stop" >&2; exit 1; }
  args=$(echo "$args" | sed -E "s/-var $var [^ ]+//")" -var $var $val"
done
case " $args " in *" -var seed "*) ;; *) echo "note: no seed given; the input's default seed is used (the cases used seed=11)" >&2 ;; esac
work=$(mktemp -d); trap 'rm -rf "$work"' EXIT
cp -R "$src" "$work/case"
cd "$work/case/$sub"
rm -f log.lammps lammps.out analysis.out ./*.profile ./*.dat ./*.png ./*params.txt
echo "$(date +%T) $case_name: $MPIRUN -np $NP $LMP -in $input $args"
# shellcheck disable=SC2086  # $args is a list of -var arguments
"$MPIRUN" -np "$NP" "$LMP" -in "$input" $args < /dev/null > lammps.out 2>&1 || { echo "LAMMPS failed: see $out" >&2; cp -R "$work/case" "$out"; exit 1; }
MPLBACKEND=Agg "$PYTHON" "$analysis" < /dev/null > analysis.out 2>&1 || echo "[exit code $?]" >> analysis.out
mkdir -p "$(dirname "$out")"
cp -R "$work/case" "$out"
find "$out" \( -name '*.lammpstrj' -o -name '*.xyz' -o -name '__pycache__' \) -prune -exec rm -rf {} +
echo "$(date +%T) $case_name: done; outputs in $out"
