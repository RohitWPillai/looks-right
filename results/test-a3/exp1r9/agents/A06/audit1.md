verdict: untrusted
run: none
cause: T*=1.5 is above the liquid-vapour critical temperature of the Lennard-Jones fluid (about 1.19 for this truncated rc=2.5 potential, about 1.31 for the full potential), so the slab dissolved into a single fluid with no interface, and no run at the purpose's temperature can bring one back.
evidence: command.txt (-var T 1.5) and slab_params.txt (T 1.5, rcut 2.5); analysis.out reports "SLAB EVAPORATED / no two-phase coexistence (rho_liq=0.322, rho_liq/rho_vap=2.3)" and no gamma; in log.lammps production, pxx, pyy and pzz agree within noise (step 100000: 0.266/0.261/0.274), so the pressure is isotropic.
