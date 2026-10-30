I can't trust this measurement. The equilibration was too short, so the first part of the production run sampled a slab that was still settling. The reported surface tension averages over that drift.

verdict: untrusted
run: nequil=60000
cause: Production began before the slab had equilibrated, so the surface tension averages in a non-stationary stretch, probably the starting FCC slab still melting; a longer equilibration with the same purpose fixes this.
evidence: In log.lammps the potential energy per atom keeps rising through production, from -4.45 at step 0 to about -4.05 by step 25000–30000, then levels off within ±0.05; the run used nequil=10000 (slab_params.txt, command.txt); the liquid density in slab_density.profile alternates between about 0.700 and 0.715 roughly every σ, a sign of leftover layering; the liquid region in slab_pressure.png shows P_N and P_T swinging by about ±0.04; analysis.out reports γ=0.261 from one run of 100000 steps, so about a quarter of the average is unrelaxed and the bias may match or exceed the single-run scatter.
