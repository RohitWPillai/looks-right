Checked the new run's log and profile; here is the final answer.

verdict: trusted
use: new
cause: With 80000 equilibration steps the fluid reached the T* 1.0 wall baths before production began and stayed there throughout, so the new profile is an equilibrium average with resolved, symmetric wall layering, while the original's contact peaks were biased low (up to ~2.5%) by the warming fluid.
evidence: new/log.lammps: thermo temp plateaus at ~0.83–0.84 by equilibration step ~50000 and stays flat at 0.83–0.87 over all 50000 production steps (PE steady at about −23.78 to −23.82, no drift); new/day1_density.profile: contact peaks 1.497 (bottom, z≈3.25) and 1.501 (top, z≈20.56), within 0.3% of each other, second layers 0.966/0.977, bulk ~0.72 (new/analysis.out: rho_bulk 0.720, peak 1.501, contrast 2.09x); original/day1_density.profile and original/analysis.out: peaks 1.481/1.463, a 1.2% top-to-bottom gap, bulk 0.725, contrast 2.04x, so the new peaks are 1–2.5% higher, more than the run-to-run scatter.
