verdict: untrusted
run: vwall=0.5
cause: The run used vwall=3.0 instead of the input's gentle default of 0.5, and viscous heating raised the fluid to T≈2.2 at the walls and T≈3.2 at the centre, so the measured η≈0.978 belongs to a hot liquid with a temperature gradient, not the isothermal LJ liquid at T*=1.0.
evidence: command.txt (-var vwall 3.0 -var seed 11); viscosity.in:31 (vwall default 0.5, "gentle = linear regime"); analysis.out (dvx/dz=0.3532, pxz=-0.3455, eta≈0.978, T(z) walls ~2.19/2.15, centre ~3.18); log.lammps (thermo temp ≈3.7 throughout production, against Tbot=Ttop=1.0).
