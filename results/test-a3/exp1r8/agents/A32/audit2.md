verdict: trusted
use: new
cause: The new run differs only in using the intended 0.1σ bins, and they resolve clear near-wall layering at both walls, peaking at about 2× the bulk density, far above the roughly 2% bin-to-bin scatter; the bulk density of about 0.725 matches the original run, so the original's flat profile came from its 1σ bins.
evidence: new/command.txt `-var binw 0.1 -var seed 11`; new/log.lammps:319 bin width 0.100046σ (238 bins), Tbot = Ttop = 1.0, both runs (20000 equilibration and 50000 production steps) complete with no warnings; new/day1_density.profile peaks 1.481 at z≈3.25 and 1.463 at z≈20.56, minima ≈0.37, fading oscillations to a flat bulk of 0.70–0.75; new/analysis.out rho_bulk ~0.725, peak ~1.481, contrast 2.04x (original: 0.725, 0.736, 1.02x).
