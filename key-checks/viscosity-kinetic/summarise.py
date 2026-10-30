"""What: summary of the viscosity key check (9 Oct 2026): the kinetic part of the shear stress beside the pair part.
Who runs it, from this folder:  python3 summarise.py   (the runs: see README.md)
Refuses: nothing; reports a seed as NOT SAME if its pair-stress series differs from the earlier replica run's.
"""
import filecmp
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
REPLICAS = HERE  # replica-s<seed>/day1_stress.dat: the earlier replica runs' pair stress, for the comparison
N_FLUID = 3920  # fluid atoms (log.lammps of the replica runs)
VF = 23.811 * 12.699 * 18.918  # the input's Vf: box lx * ly * fixed height


def block_se(x, nblocks=10):
    blocks = np.array_split(x, nblocks)
    means = np.array([b.mean() for b in blocks])
    return means.std(ddof=1) / np.sqrt(nblocks)


print("| seed | pair series same as replica | pair p_xz | kinetic p_xz | kinetic / pair | kinetic xx / zz | fluid T from zz |")
print("|---|---|---|---|---|---|---|")
for seed in (11, 22, 33):
    run = HERE / f"run-s{seed}" / "viscosity"
    d = np.loadtxt(run / "day1_stress_kinetic.dat")
    pair, kin, xx, zz = d[:, 1], d[:, 2], d[:, 3], d[:, 4]
    same = filecmp.cmp(run / "day1_stress.dat",
                       REPLICAS / f"replica-s{seed}" / "day1_stress.dat", shallow=False)
    t_z = zz.mean() * VF / N_FLUID
    ratio = kin.mean() / pair.mean()
    print(f"| {seed} | {'same' if same else 'NOT SAME'} | {pair.mean():.4f} ± {block_se(pair):.4f} | "
          f"{kin.mean():.5f} ± {block_se(kin):.5f} | {100 * ratio:.1f}% | {xx.mean() / zz.mean():.3f} | {t_z:.3f} |")
