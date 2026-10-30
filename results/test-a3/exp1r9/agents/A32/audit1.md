verdict: untrusted
run: binw=0.1
cause: The run was launched with `-var binw 1.0`, which makes each bin about 0.99σ wide, roughly one layer spacing, so the near-wall density peaks are averaged away and the profile looks flat; a 0.1σ bin would show the layering, and the peaks should be much larger than the ~0.01 bin-to-bin scatter.
evidence: command.txt (`-var binw 1.0 -var seed 11`); log.lammps line 319 (bin width 0.992125657480125, 24 chunks); day1_density.profile (fluid bins 4–21 range 0.715–0.736, bulk ~0.725, no oscillation); analysis.out (bulk 0.725, peak 0.736, contrast 1.02x, "no layering left"); density.in line 22 (default binw 0.1 "resolves the near-wall layers; coarsen to wash them out").
