verdict: untrusted
run: gforce=0.2 nprod=800000
cause: At gforce 0.05 in a 4σ pore the flow signal (centre vx ≈ 0.02, near-wall ≈ 0.002) is about the same size as the bin-to-bin noise (≈ 0.01 per 0.1σ bin), so dvx/dz and therefore eta(z) are mostly noise; the "no single plateau" result cannot tell real non-Newtonian layering from noise, and quadrupling the drive with 4× the production steps raises the signal-to-noise about 8× while keeping the shear rate ≲0.1.
evidence: poiseuille_w4.profile vx column (0.0019–0.029, no clear parabola, e.g. bin 33 0.0176, bin 38 0.0290, bin 39 0.0143); analysis.out (3 layers, "NO single plateau"); params gforce 0.05, w_meas 4; log.lammps c_Tprof ≈ 1.00, no lost atoms, 308k total steps, so 908k for the new run is within the 4× limit.
