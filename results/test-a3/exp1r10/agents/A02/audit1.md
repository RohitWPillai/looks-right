verdict: untrusted
run: vwall=0.5
cause: The run used vwall=3.0 instead of the input's default of 0.5, and the resulting viscous heating took the fluid from the T* of 1.0 the purpose states to about 2.2 at the walls and 3.2 at the centre, so η≈0.978 belongs to a hot, non-isothermal fluid, not the T* 1.0 liquid; at vwall=0.5 the shear rate falls about 6× and the heating, which scales with its square, about 36×.
evidence: command.txt (-var vwall 3.0, seed 11), viscosity.in:31 (the default vwall is 0.5, commented "gentle = linear regime"), analysis.out (dvx/dz=0.3532, pxz=-0.3455, η≈0.978, T(z) walls 2.19/2.15, centre 3.18), log.lammps (thermo Temp ≈3.7–3.8 through production).
