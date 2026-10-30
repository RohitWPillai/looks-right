Checked the profile against the expected flow signal. The verdict:

verdict: untrusted
run: gforce=0.5
cause: At gforce 0.05, flow across the 4σ pore is about the same size as thermal noise, so dvx/dz and eta(z) are mostly noise; the "no single plateau" result can't be told apart from noise. At 10× the force the slopes come out clearly, with shear rate still around 0.1–0.2, well inside the Newtonian range.
evidence: In poiseuille_w4.profile, vx stays between 0.002 and 0.029 in every fluid bin and jumps ±0.01 between neighbouring 0.1σ bins (e.g. 0.0289→0.0143→0.0098 at z 3.73–3.93, and 0.0167 vs 0.0248 at symmetric bins), with no parabola. Slope noise is about 0.01/0.1 ≈ 0.1, against an expected wall slope of about ρg·h/(2η) ≈ 0.03 and a peak vx of ≈ 0.02. The setup itself is fine: log.lammps shows c_Tprof ≈ 1.00, rho_acc = 0.800, w_meas = 4 and 0 dangerous builds, and analysis.out's mean density is 0.860 with 3 layers.
