Done reading: equilibration was too short. The slab started as a crystal and was still melting during the first ~40% of production, so I'm judging the result untrusted.

verdict: untrusted
run: nequil=80000 nprod=300000
cause: The FCC-seeded slab was still melting well into production (the potential energy kept rising for about the first 40,000 production steps), so the time-averaged pressure tensor mixes in the stresses of a partly crystalline slab, which biases γ by more than its run-to-run scatter (about ±0.05).
evidence: log.lammps shows PE at −6.00 after minimisation and −4.45 at the end of the 10,000-step equilibration, then a steady climb in production (−4.33 at 1k, −4.23 at 10k, about −4.15 at 20k), levelling off near −4.05 only after about 40–50k steps. analysis.out gives γ=0.261 from one 100,000-step window averaged over the whole of production (nfreq=nprod in the input, so the transient can't be dropped afterwards). The density profile (ρl=0.706, ρv=0.021) and the bulk pressures (about 0.02) look sensible, which hides the problem. The proposed run uses 380,000 steps, within 4× the original 110,000.
