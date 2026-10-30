verdict: untrusted
run: binw=0.1
cause: The run used `-var binw 1.0`, which makes each bin about one σ wide, the same as the spacing between wall layers, so the layering is averaged away and the "no layering, 1.02x contrast" result comes from the bins, not the liquid.
evidence: command.txt sets `binw 1.0` while density.in's default is 0.1 ("0.1 resolves the near-wall layers; coarsen to wash them out"). day1_density.profile has 24 bins of 0.99σ, reading ~0.72–0.736 flat from z≈3.5 to 20.3. analysis.out reports rho_bulk ~0.725 and a near-wall peak of 0.736 (1.02x); with 0.1σ bins the first wall peak should be several times the bulk value, far above the ~0.005 scatter between bins.
