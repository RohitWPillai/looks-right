verdict: untrusted
run: binw=0.1
cause: The run used -var binw 1.0, so each density bin is about one fluid diameter wide; that averages the wall layers (spacing about 1 sigma) together, so the "no layering" result comes from the binning, not from the liquid.
evidence: command.txt has "-var binw 1.0" (the input's default is 0.1, and its comment says to coarsen it "to wash them out"); day1_density.profile has 24 bins about 0.99 sigma wide, with only 0.715 to 0.736 between the walls; analysis.out reports bulk ~0.725, peak ~0.736 and contrast 1.02x ("no layering left"); log.lammps shows no errors and both runs finished (20000 + 50000 steps).
