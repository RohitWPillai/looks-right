verdict: untrusted
run: vwall=0.5
cause: The run was driven at vwall 3.0 (command.txt) instead of the input's gentle default of 0.5, so viscous heating made the fluid about 2.2–3.2 instead of 1.0, and the measured 0.978 is the viscosity of a much hotter, non-uniform liquid rather than at T* 1.0; at vwall 0.5 the heating, which grows with the square of the shear rate, would be about 36× smaller.
evidence: command.txt `-var vwall 3.0`; viscosity.in default `vwall index 0.5` ("gentle = linear regime") and baths Tbot=Ttop=1.0; analysis.out shear rate 0.3532, pxz −0.3455, eta ≈ 0.978, T(z) about 2.19/2.15 at the walls and 3.18 at the centre (a viscous-heating hump); log.lammps thermo temp about 3.8 throughout the run.
