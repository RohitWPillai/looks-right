# Pore key check: thermostat bins (9 Oct 2026)

**Question.** In Test A2 the Auditor asked for a ten times weaker fluid thermostat on the 10 sigma pore, and the
plateau viscosity fell from 2.528, 2.422 and 2.482 (seeds 11, 22, 33; `cases/pore-base`,
`results/test-a2/replica-analysis/`) to 2.104, 2.148 and 2.163 (`results/reruns/A20-run`, `A04-run`, `A35-run`;
`key/HISTORY.md`). Is the course's plateau biased high because its 1 sigma temperature bins let the thermostat damp
part of the flow?

**Test.** The same input with 0.25 sigma temperature bins (`sim/shared_setup.lmp` line 154, the only change;
damping unchanged), seeds 11, 22, 33, 8 MPI ranks (`run-s<seed>/`). Rerun recipe: `key-checks/README.md`.

**Result** (`run-s<seed>/poiseuille/analysis.out`): plateau 2.350, 2.406, 2.317. Finer bins remove 42%, 6% and 52%
of the three seeds' drops, so they explain part of the drop at most. The rest of the dependence on thermostat
strength remains, cause not established. The key for the pore Follow run was not changed.
