verdict: untrusted
run: vwall=0.5
cause: The run used wall speed 3.0 (six times the 0.5 that the input file comments call the linear regime), and viscous heating took the fluid to about 2.2–3.2 instead of T* 1.0, so eta ≈ 0.98 is the viscosity of a much hotter fluid; the expected value at T* 1.0 (about 1.7–2) differs by far more than the run-to-run scatter.
evidence: command.txt (-var vwall 3.0), day1_params.txt (vwall 3.0), analysis.out (T(z) is 2.19/2.15 at the walls and 3.18 at the centre, dvx/dz 0.3532, pxz -0.3455, eta 0.978), and log.lammps (temp column about 3.7–3.8 through production, which also counts the flow velocity).
