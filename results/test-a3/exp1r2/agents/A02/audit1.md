verdict: untrusted
run: vwall=0.5 nprod=200000
cause: The run used a wall speed of 3.0 (the input's default is 0.5), and the resulting viscous heating put the fluid at about T* 2.2–3.2 instead of T* 1.0, so the reported viscosity of 0.978 belongs to a hotter, non-isothermal liquid; the LJ liquid at T* 1.0 should have a viscosity near 2, which is a far bigger gap than run-to-run scatter.
evidence: command.txt (-var vwall 3.0); analysis.out (fluid T(z) at the walls ~2.19/2.15, centre ~3.18; dvx/dz=0.3532, pxz=-0.3455, eta~0.978); log.lammps (thermo temp ~3.7 throughout production, which is inflated by the moving walls but agrees with the heating); viscosity.in default vwall 0.5 is commented "gentle = linear regime".
