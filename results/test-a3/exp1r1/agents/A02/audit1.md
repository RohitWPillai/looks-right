verdict: untrusted
run: vwall=0.5 nprod=260000
cause: The run used wall speed 3.0 instead of the gentle default of 0.5, so viscous heating raised the fluid to about T 2.2–3.2 instead of 1.0; this, plus strong shear (rate 0.35), shifts eta by tens of percent, far more than run-to-run scatter.
evidence: The command line in command.txt sets `-var vwall 3.0` (viscosity.in defaults to 0.5, "gentle = linear regime"); analysis.out reports T(z) of about 2.19/2.15 at the walls and 3.18 at the centre, shear rate +0.3532, pxz -0.3455 and eta about 0.978; in log.lammps the thermo temperature climbs from 1.32 to about 3.8 during equilibration and stays there in production. The longer nprod (total 280000 steps, 4× the original 70000) offsets the smaller signal at about 1/6 the shear rate.
