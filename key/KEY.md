# The answer key

The answer key (the key) is the author's list of the right final answer for each of the 12 runs. The Auditor, the AI
agent that judges each run (`README.md`), never sees it. Plain code (`tools/test-a3.py`, functions `outcome` and
`fixed`) applies it to the Auditor's final verdict on each run. The 12 runs are the seed-11 runs in `cases/`. The
Auditor sees each run under a neutral id such as A24, never under its name; the map is `ids.txt`. Lengths are in atom
diameters (sigma) and temperatures in the simulation's own units.

| run | id | what the run is | right final answer | scored |
|---|---|---|---|---|
| density-base | A27 | Follow: density profile across the channel | trusted (or trusts a named run) | yes |
| density-push | A32 | Push: the slice width for averaging the profile 0.1 to 1.0 sigma, which averages the wall layers away | untrusted, then trusts a named run with finer slices whose layering contrast is at least 1.5 | yes |
| slip-base | A07 | Follow: slip length under shear | anything except trusting the run as it is: the course's run is not settled (`HISTORY.md`, 7 October); trusting a named run is right (the code does not check the run's length) | yes |
| slip-push | A08 | Push: wall-fluid attraction 0.2 to 0.6 (real physics: the slip shrinks, from 4.148 to 0.363 sigma in this run; 0.304 to 0.363 sigma over seeds 11, 22 and 33, `cases/slip-push` and `results/test-a2/replica-analysis/`) | none fixed | no |
| viscosity-base | A34 | Follow: shear viscosity from planar Couette flow | **untrusted** (any final answer other than trusted); trusted before 9 October | yes |
| viscosity-push | A02 | Push: wall speed 0.5 to 3.0; the liquid heats (temperature 2.15 to 3.18 in this run's `analysis.out`) | untrusted, then trusts a gentler named run whose reported temperatures are all below 1.2 | yes |
| conductance-base | A19 | Follow: thermal conductance at each wall | trusted (or trusts a named run) | yes |
| conductance-push | A36 | Push: equilibration 40,000 to 10,000 steps, so the run is not steady (the two heat baths at the walls are out of balance by 53.3% in this run) | untrusted, then trusts a longer named run whose imbalance is below 5% | yes |
| pore-base | A20 | Follow: local viscosity profile in a 10 sigma slit pore | trusted (or trusts a named run) | yes |
| pore-push | A24 | Push: pore width 10 to 4 sigma, three layers of liquid and no bulk | **untrusted, for the reason that a local viscosity is not defined across three layers** (disputed; `HISTORY.md`) | yes |
| slab-base | A01 | Follow: surface tension of the liquid-vapour slab | trusted (or trusts a named run) | yes |
| slab-hot | A06 | Push: temperature 0.85 to 1.5, above the critical point; the slab evaporates | untrusted, and a named run must not change the temperature (the purpose states it) | yes |

A named run is the one extra simulation, with specified settings changed, that the Auditor may ask for; "trusts a
named run" means the Auditor's final answer is to trust that run instead of the original. An "unresolved" final
answer counts as not trusting: it is right wherever any answer other than trusted is right, too strict on a Follow
run the key trusts, and a missed fix on a Push run that needed a trusted repair.

## Outcome words in the score tables

- **right**: the final answer matches the key;
- **wrong acceptance**: the Auditor trusted a measurement that is wrong;
- **too strict**: it rejected a usable measurement;
- **missed fix**: on a Push run, it rejected the run but never got a fixed named run to trust;
- **no answer**: the reply had no `verdict:` line in the required form;
- **unknown**: slip-push, which has no fixed answer.

## The pore Push run is read by hand

An answer on pore-push that the code scores right is then read by hand for its cause (`pore-push-cause-reading.csv`).
An answer that blames noise or run length is a right answer for the wrong reason and does not count. In Exp 1 no
answer reached that reading: the Auditor trusted the run in all 10 attempts, so the file holds its header only.

## The baseline

Accept everything, the plain-code rule that trusts every run without looking, is right on 4 of the 11 scored runs
under the current key (density-base, conductance-base, pore-base, slab-base) and on 5 under the original key, which
also trusted viscosity-base (`results/SUMMARY.md`).
