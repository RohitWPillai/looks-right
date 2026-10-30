# Checks on the answer key

The answer key (the key) is the author's list of the right final answer for each run (`key/KEY.md`). These are
plain-code simulation runs made to test the key itself, outside the experiments. No AI agent takes part. Each folder
has its own README with the inputs, the runs and the numbers. Lengths are in atom diameters (sigma).

| folder | question | result | effect on the key |
|---|---|---|---|
| `viscosity-kinetic/` | Does the course's viscosity input leave out the kinetic part of the shear stress (the momentum the moving atoms carry), as the Auditors said, and keep only the pair part (the forces between atoms)? | yes: the kinetic part is 11.6%, 12.4% and 12.5% of the pair part on seeds 11, 22 and 33 (`viscosity-kinetic/SUMMARY.md`) | viscosity-base changed from trusted to untrusted, 9 October 2026 (`key/HISTORY.md`) |
| `pore-thermostat/` | Is the 10 sigma pore's plateau viscosity biased because the thermostat (which holds the liquid at its set temperature) works in 1 sigma slices? | partly at most: 0.25 sigma slices give 2.350, 2.406 and 2.317 on seeds 11, 22 and 33, removing 42%, 6% and 52% of each seed's drop under a weaker thermostat (`pore-thermostat/README.md`) | none |
| `pore-scan/` | At which pore widths is a local viscosity (a viscosity defined at each height across the pore) defined? Seven widths, three seeds, each run analysed 144 ways | the rule set before the runs did not separate the widths (`pore-scan/RESULT.md`) | none; the 4 sigma key stays disputed |

## Rerunning the checks

`viscosity-kinetic/` and `pore-scan/` give their own rerun commands in their READMEs. The thermostat check cannot be
rerun with `tools/run-case.sh`, which uses the course's original input; it uses its own copy of the pore input with
one line changed (`pore-thermostat/sim/shared_setup.lmp`, line 154: 0.25 sigma temperature slices instead of 1.0).
To repeat it for one seed, with an MPI build of LAMMPS on the PATH:

```
cp -R key-checks/pore-thermostat/sim /tmp/thermostat-s11
cd /tmp/thermostat-s11/poiseuille
mpirun -np 8 lmp_mpi -in poiseuille.in -var seed 11 > lammps.out 2>&1
python3 analyse_poiseuille.py > analysis.out
```

Repeat with `-var seed 22` and `-var seed 33`. The plateau viscosity is the "eta(z) plateau (mid-pore)" line of
`analysis.out`; compare with `pore-thermostat/run-s<seed>/poiseuille/analysis.out`. About 50 s per run on 8 ranks.
