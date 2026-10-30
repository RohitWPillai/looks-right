# Pore definition scan (26 Oct 2026)

**Question.** At which slit-pore widths is a local viscosity defined? This bears on the disputed 4 sigma pore key.

**Runs.** The course's pore input at widths 4, 5, 6, 7, 8, 10 and 12 sigma, seeds 11, 22, 33, 2,000,000 production
steps each (`runs.txt`: one line per run, as `NAME=VALUE` changes to the pore-base case; rerun one with
`bash tools/run-case.sh pore-base <folder> width=4 seed=11 nprod=2000000`). Shipped per run: the profile, the
parameters and the analysis output (`runs/`); the LAMMPS logs are left out.

**Analysis.** `scan-b.py` analyses each run 144 ways (shear-rate route, bin merging, centreline mask, region next to
the walls, median or mean), with the course's own formulas imported from `cases/pore-base/`. Rule, fixed before the
runs: a width is "sensitive" when any choice's three-seed mean differs from the default's by more than the default's
95% half-width, or gives no answer. Regenerate `RESULT.md` and `eta-by-width.png` with `python3 scan-b.py`.

**Result** (`RESULT.md`): default viscosity 2.192 ± 0.542 (4 sigma), 2.676 ± 0.582 (5), 2.772 ± 0.845 (6),
2.372 ± 0.420 (7), 2.429 ± 0.233 (8), 2.462 ± 0.062 (10), 2.421 ± 0.168 (12). By the rule: sensitive at 4, 5, 7, 8,
10 and 12 sigma, no sensitivity detected at 6. The prediction written before the runs (sensitive at 4 and 5, not at 7
and wider) was not met: the rule does not separate the widths. The largest moves are much larger at 4 sigma than at
8 to 12, but that pattern was read after the fact and is not a result.
