# The 12 runs

A run is one finished molecular dynamics simulation: its LAMMPS input, its log, and the result the course's analysis
script computed from it. The 12 runs here are six measurements from the hands-on course of the NEMD 2026 summer
school (https://github.com/Non-Equilibrium-Molecular-Dynamics/NEMD-Summer-School-2026). Each measurement was run
twice: once exactly as the course instructs (the Follow run, folder `-base`) and once with one setting deliberately
changed to challenge the measurement (the Push run, folder `-push`; for the liquid-vapour slab the Push run is
`slab-hot`, the slab heated above its critical temperature). All 12 use seed 11 (the seed is the number that sets a
run's random starting velocities) and were run on a Mac mini with 8 MPI ranks (8 processes working on one run) under
LAMMPS 22 Jul 2025 Update 5. These are the exact runs every attempt of Exp 1 judged. The same runs at seeds 22 and 33,
from an earlier unreleased test, are kept as the key's evidence (their analysis output is in
`results/test-a2/replica-analysis/`; `key/HISTORY.md`). Lengths are in atom diameters (sigma) and temperatures in
the simulation's own units.

| folder | course sheet | the Push run's changed setting | command (from the run's subfolder) | wall time |
|---|---|---|---|---|
| `density-base` | Day 1, LJ channel: density profile and layering next to the walls | | `mpirun -np 8 lmp_mpi -in density.in -var seed 11` | 0:00:14 |
| `density-push` | same | slice width for averaging the profile 0.1 to 1.0 sigma | `... -in density.in -var binw 1.0 -var seed 11` | 0:00:15 |
| `slip-base` | Day 1, slip length (the depth inside the wall at which the liquid's velocity profile, extended in a straight line, reaches the wall's speed) | | `... -in slip.in -var seed 11` | 0:00:51 |
| `slip-push` | same | wall-fluid attraction 0.2 to 0.6 (real physics, not a fault; no fixed right answer) | `... -in slip.in -var eps_wf 0.6 -var seed 11` | 0:00:52 |
| `viscosity-base` | Day 1, shear viscosity from planar Couette flow (one wall dragged past the other) | | `... -in viscosity.in -var seed 11` | 0:00:15 |
| `viscosity-push` | same | wall speed 0.5 to 3.0 | `... -in viscosity.in -var vwall 3.0 -var seed 11` | 0:00:21 |
| `conductance-base` | Day 1, interfacial thermal conductance (heat flow from each wall into the liquid) | | `... -in conductance.in -var seed 11` | 0:00:17 |
| `conductance-push` | same | equilibration (settling-in) steps 40,000 to 10,000 | `... -in conductance.in -var nequil 10000 -var seed 11` | 0:00:10 |
| `pore-base` | Day 2, slit pore (a narrow gap between two walls), Poiseuille flow driven by a force on every atom, local viscosity at each height | | `... -in poiseuille.in -var seed 11` | 0:00:48 |
| `pore-push` | same | pore width 10 to 4 sigma | `... -in poiseuille.in -var width 4 -var seed 11` | 0:00:25 |
| `slab-base` | Day 2, liquid-vapour slab, surface tension | | `... -in liquid_vapour.in -var localstress 1 -var seed 11` | 0:00:25 |
| `slab-hot` | same | temperature 0.85 to 1.5, above the critical point | `... -in liquid_vapour.in -var localstress 1 -var T 1.5 -var seed 11` | 0:00:10 |

Wall times are from each `log.lammps`. Rerun one with `bash tools/run-case.sh <folder> <new folder> seed=11`
(`REPRODUCE.md`, level 2).

## Rerunning a named run

The Auditor saw each run under a neutral id (`key/ids.txt`: A24 is `rep-pore-push-s11`, that is `pore-push` at seed
11), and its named runs are recorded per attempt in `results/test-a3/<try>/runs-checked.txt` as `NAME=VALUE` changes to
that run. For example, Exp 1 attempt 1 records `A24: gforce=0.2 nprod=1000000 seed=12`; to repeat that run:

```
bash tools/run-case.sh pore-push /tmp/exp1r1-A24 gforce=0.2 nprod=1000000 seed=12
```

Its analysis output as recorded during the experiment is `results/reruns/exp1r1-A24-run/poiseuille/analysis.out`.

## Layout of a run folder

The layout follows the course. The Day 1 runs and the Day 2 slit-pore runs keep `shared_setup.lmp` (the part of the
input shared by the Day 1 sheets) and `lammps_io.py` (the course's file reader) at the top, and the input, the
analysis script (`analyse_*.py`) and every output in a subfolder; the slab runs are flat. Each run holds: the LAMMPS
input, `log.lammps`, `lammps.out` (the screen output), `analysis.out` (the output of the course's analysis script),
the profiles and data files, and the course's plots. The inputs carry the course's own comments, including its
teaching hints; the Auditor saw a copy with the hints removed (`auditor/README.md`).

`slab-base/intrinsic_surface.py` and `slab-hot/intrinsic_surface.py` are an optional extra from the course and do not
run on their own here: they import `view_domain.py`, which is at the top level of the course repository. The main slab
analysis (`analyse_liquid_vapour.py`) does not need them.

## What was left out of each run folder

Each run folder was copied back from the Mac mini; for every Day 1 run the course's whole Day 1 folder was copied.
Left out of this release: the course handouts (`day1-handout.pdf`, 1.06 MB, and `setup-cirrus.pdf`, 0.27 MB, per
Day 1 run; both public in the course repository), three screenshots of the course website (0.33 MB per run), local
editor and browser-tool settings and logs (`.claude/`, `.playwright-mcp/`, `.DS_Store`), the other Day 1 sheets'
inputs (identical to their own runs'), `clean.sh`, `lmp.log`, `nano2.json`, a 65-byte stub `log.lammps` at the
folder's top, and the slab's optional `ensemble/` job script for a cluster. Trajectory dumps (`*.lammpstrj`, `*.xyz`),
if any, were never copied back from the Mac mini. In all, about 1.9 MB per Day 1 run was left out, none of it read by the Auditor or used by the
scorer.
