Checked the new run: its profile is smooth and symmetric, the temperature holds, and the conclusion is unchanged. Here's the answer.

verdict: trusted
use: new
cause: At gforce 0.2 the velocity profile is now smooth and mirror-symmetric, so it resolves dvx/dz well above the noise, and it gives the same result as the original: 3 wall-induced layers and no single eta(z) plateau, i.e. no local Newtonian viscosity across the 4σ pore.
evidence: new/poiseuille_w4.profile vx rises smoothly from 0.005 (bin 31) to 0.046 (bin 33), 0.068 (bin 35) and about 0.10 at the centre (bin 45), with mirror bins matching to within about 0.005 (33/56: 0.0460/0.0457, 35/54: 0.0676/0.0718); density peaks are 1.695/1.701 (bins 33/56) and 1.208/1.204 (bins 44/45); new/analysis.out shows "3 wall-induced layer(s)", "NO single plateau" and centre density 0.759, against 0.758 in original/analysis.out; new/log.lammps c_Tprof stays about 0.92–1.09 (≈1.0) through 800000 steps with 2646 atoms throughout; new/command.txt is gforce 0.2, nprod 800000.
