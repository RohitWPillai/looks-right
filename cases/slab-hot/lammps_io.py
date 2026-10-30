"""Shared output-parsing helpers for the Day-2 Part-2 (L-V slab) analysers.

The slab run writes two `fix ave/chunk` files binned along z: a 4-column density
profile (slab_density.profile) and a 9-column stress profile (slab_stress.profile,
the six diagonal virial + kinetic sums). Both are parsed here so
analyse_liquid_vapour.py and intrinsic_surface.py read LAMMPS output identically.

Import from the same folder you run in:

    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from lammps_io import read_profile, read_stress_profile, read_params
"""
import os
import sys
import tempfile

import numpy as np

# Point matplotlib's cache at a writable dir BEFORE any analyser imports matplotlib,
# so a non-writable $HOME on Cirrus does not error or rebuild the font cache each run.
os.environ.setdefault("MPLCONFIGDIR", os.path.join(tempfile.gettempdir(), "day2_mplcache"))


def _last_block(path, mincols):
    """Rows of the LAST complete `fix ave/chunk` block -> 2-D array (>= mincols columns).

    Each block is a 2+-token header (timestep n_chunks [total]; only n_chunks is
    used) followed by n_chunks data rows. A trailing block that is short, has a
    truncated row, or a value cut mid-number (a run still writing / killed
    mid-write) is dropped, so the last COMPLETE block is returned."""
    with open(path) as f:
        lines = [l for l in f if not l.startswith("#") and l.strip()]
    blocks, i = [], 0
    while i < len(lines):
        try:
            n = int(lines[i].split()[1])                       # block header: timestep n_chunks [total]
        except (ValueError, IndexError):
            break
        if n <= 0 or i + 1 + n > len(lines):
            break                                              # trailing block not fully written
        rows, ok = [], True
        for k in range(n):
            c = lines[i + 1 + k].split()
            if len(c) < mincols:                               # row truncated at a column boundary
                ok = False
                break
            try:
                rows.append([float(x) for x in c[:mincols]])
            except ValueError:                                 # a value cut mid-number
                ok = False
                break
        if not ok:
            break
        blocks.append(np.array(rows))
        i += 1 + n
    if not blocks:
        sys.exit(f"{path}: no complete data block - the run may still be writing, was killed "
                 f"mid-write, or is too short. Wait for the job to finish (squeue --me) or rerun.")
    return blocks[-1]


def read_profile(path):
    """Density `fix ave/chunk` file -> (z, Ncount, density) of the last complete block."""
    a = _last_block(path, 4)
    return a[:, 1], a[:, 2], a[:, 3]                            # Coord1, Ncount, density/number


def read_stress_profile(path):
    """Stress `fix ave/chunk` file -> (z, Ncount, S) of the last complete block.

    S is (n_bins, 6): columns [virial_xx, virial_yy, virial_zz, kinetic_xx,
    kinetic_yy, kinetic_zz], each SUMMED over the bin's atoms (the run uses
    `norm none`). The analyser combines and volume-normalises these into the
    diagonal pressure tensor."""
    a = _last_block(path, 9)
    return a[:, 1], a[:, 2], a[:, 3:9]                          # Coord1, Ncount, six stress sums


def read_params(path):
    """Read a `key value` text file (slab_params.txt) -> {key: float}.

    Lines whose second token is non-numeric are skipped, so any header/comment
    line does no harm."""
    p = {}
    with open(path) as f:
        for l in f:
            t = l.split()
            if len(t) >= 2:
                try:
                    p[t[0]] = float(t[1])
                except ValueError:
                    pass
    return p
