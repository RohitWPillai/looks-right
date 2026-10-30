verdict: untrusted
run: binw=0.1
cause: The run was launched with `-var binw 1.0`, a bin about as wide as the spacing between layers (~1σ), so averaging over each bin flattens the wall layering; 0.1σ bins, the input's own default, would show it.
evidence: command.txt has `-var binw 1.0`. day1_density.profile has only 24 bins, ~0.99σ wide, and the fluid fills bins 4–21 at a flat 0.715–0.736. analysis.out reports bulk 0.725, peak 0.736 and a "layering contrast 1.02x", which comes from the coarse bins, not the physics. log.lammps shows no errors and a full 20000+50000-step run, but density.in's comment says "0.1 resolves the near-wall layers; coarsen to wash them out".
