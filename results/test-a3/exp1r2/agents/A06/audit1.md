verdict: untrusted
run: none
cause: At T*=1.5, set via `-var T 1.5`, the run is above the liquid-vapour critical temperature of the Lennard-Jones fluid: about 1.1–1.2 with this 2.5σ cutoff, and about 1.31 even with no cutoff. With no interface to measure, no surface tension exists to report, and no run that keeps this temperature can fix that.
evidence: command.txt shows T=1.5 and slab_params.txt shows rcut=2.5; analysis.out reports the slab evaporated (rho_liq=0.322, rho_liq/rho_vap=2.3, no gamma reported); slab_density.profile shows a smooth hump from about 0.13 to 0.33 over roughly 60σ with no liquid plateau, although the run started from a liquid at 0.7.
