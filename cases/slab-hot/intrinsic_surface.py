#!/usr/bin/env python3
"""Day 2 - Part 2: the intrinsic (capillary-wave) surface of the slab.

A lab-frame density profile smears the liquid-vapour interface because thermal
capillary waves move the surface up and down. This script fits the instantaneous
surface from the liquid atoms (a Fourier-mode expansion, the approach Sega's
pytim implements) and re-bins the density relative to that surface, so the
intrinsic layering the lab-frame average hides becomes visible.

It reads slab_traj.xyz (written by `lmp_serial -in liquid_vapour.in -var dump 1`)
and slab_params.txt for the box, and saves the lab-frame vs intrinsic density to
slab_intrinsic.png. With --show-surface it also saves one frame's fitted surface
to slab_intrinsic_surface.png.

Dependencies: numpy, matplotlib, and scikit-learn (DBSCAN, to separate the liquid
cluster from the vapour). It is single-core and O(frames x atoms x modes), so it
takes a few minutes; this is post-processing, not a Cirrus job.

Two limitations of this minimal version (acceptable for the exercise, flagged for
discussion): the DBSCAN cluster step wraps lateral coordinates but uses plain
Euclidean distance (no lateral minimum-image), and the pivot search fits the
LOWER interface only (the slab's two faces are equivalent, so one suffices).
"""
import argparse
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lammps_io import read_params                    # also sets MPLCONFIGDIR before matplotlib
from view_domain import xyz_num_frames, read_frame

# scikit-learn is imported lazily in main() AFTER the trajectory/params checks, so a
# missing slab_traj.xyz reports the actionable "run the sim first" error, not the
# optional-dependency error.
DBSCAN = None


# ---- surface-fitting core (the pytim-style algorithm; kept as the reference method) ----

def wrap_pbc(points, Lx, Ly):
    """Wrap x,y into the box [0,L)."""
    p = points.copy()
    p[:, 0] = p[:, 0] % Lx
    p[:, 1] = p[:, 1] % Ly
    return p


def liquid_vapour_dbscan(points, eps=1.5, min_samples=10, Lx=None, Ly=None):
    """Identify the liquid cluster (the largest DBSCAN cluster) -> (labels, liquid_mask)."""
    if Lx is not None and Ly is not None:
        points = wrap_pbc(points, Lx, Ly)
    clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(points)
    labels = clustering.labels_
    valid = labels >= 0
    if not np.any(valid):
        return labels, np.zeros(len(points), dtype=bool)
    liquid_label = np.argmax(np.bincount(labels[valid]))
    return labels, labels == liquid_label


def _compute_q_vectors(box, normal=2, alpha=0.5):
    """q-vectors compatible with the box. Returns (q_vectors, modes_shape, Qxy, Q)."""
    box = np.roll(box, 2 - normal)
    nmax = list(map(int, np.ceil(box[0:2] / alpha)))
    q_vectors = np.mgrid[0:nmax[0], 0:nmax[1]] * 1.0
    q_vectors[0] *= 2. * np.pi / box[0]
    q_vectors[1] *= 2. * np.pi / box[1]
    modes_shape = q_vectors[0].shape
    qx = q_vectors[0][:, 0]
    qy = q_vectors[1][0]
    Qx = np.repeat(qx, len(qy))
    Qy = np.tile(qy, len(qx))
    Qxy = np.vstack((Qx, Qy)).T
    Q = np.sqrt(np.sum(Qxy * Qxy, axis=1)[1:])
    return q_vectors, modes_shape, Qxy, Q


def get_surface_modes(points, Qxy, modes_shape, Q=None):
    if np.any(Q == None):
        Q = np.sqrt(np.sum(Qxy * Qxy, axis=1)[1:])
    QR = np.zeros([points.shape[0], Qxy.shape[0]])
    for i in range(QR.shape[0]):
        for j in range(QR.shape[1]):
            QR[i, j] = points[i, 0] * Qxy[j, 0] + points[i, 1] * Qxy[j, 1]
    ph = (np.cos(QR) + 1.j * np.sin(QR))[:, 1:]
    z = points[:, 2]
    az = np.mean(z)
    z = z - az
    A = (ph / Q)
    pinv_ph = np.linalg.pinv(A)
    s = np.zeros(modes_shape[0] * modes_shape[1] - 1, dtype=complex)
    for i in range(s.shape[0]):
        s[i] = np.dot(pinv_ph[i, :], z[:]) / Q[i]
    out = np.append(az + 0.j, s)
    return out.reshape(modes_shape)


def get_phase(point, q_vectors, derivative=None):
    dotp = q_vectors[0] * point[0] + q_vectors[1] * point[1]
    if derivative is None:
        return np.cos(dotp) + 1.j * np.sin(dotp)
    elif derivative == "x":
        return -q_vectors[0] * np.sin(dotp) + 1.j * q_vectors[0] * np.cos(dotp)
    elif derivative == "y":
        return -q_vectors[1] * np.sin(dotp) + 1.j * q_vectors[1] * np.cos(dotp)
    elif derivative in ("xy", "yx"):
        return -q_vectors[0] * q_vectors[1] * np.cos(dotp) - 1.j * q_vectors[0] * q_vectors[1] * np.sin(dotp)
    print("Error -- derivative is unknown")


def surface_from_modes(points, q_vectors, modes, derivative=None):
    elevation = []
    for point in points:
        phase = get_phase(point, q_vectors, derivative=derivative)
        elevation.append(np.sum((phase * modes).real))
    return np.array(elevation)


def get_initial_pivots(points, box, normal):
    """Nine initial pivots, one per 3x3 sector of the macroscopic plane (lowest-normal first)."""
    sorted_ind = np.argsort(points[:, normal])
    sectors = np.zeros((3, 3), dtype=int)
    pivot = []
    for ind in sorted_ind:
        part = points[ind]
        nx, ny = list(map(int, 2.999 * part[0:2] / box[0:2]))
        if sectors[nx, ny] == 0:
            pivot.append(ind)
            sectors[nx, ny] = 1
        if np.sum(sectors) >= 9:
            break
    return pivot


def update_pivots(points, q_vectors, modes, pivot, normal, alpha, tau):
    """Points within tau of the current surface fit."""
    pivot_pos = points[pivot]
    z_max = np.max(pivot_pos[:, normal]) + alpha * 2
    z_min = np.min(pivot_pos[:, normal]) - alpha * 2
    z = points[:, normal]
    candidates = np.argwhere(np.logical_and(z > z_min, z < z_max))[:, 0]
    dists = surface_from_modes(points[candidates], q_vectors, modes) - z[candidates]
    return candidates[dists * dists < tau ** 2]


# ---- driver ----

def fit_one_frame(points, box, normal, alpha, tau, ns, Ntries):
    """Fit the intrinsic surface to the liquid points of one frame.

    Returns (q_vectors, modes, liquid_pts, vapour_pts, pivot) for the lower interface."""
    labels, liquid = liquid_vapour_dbscan(points[:, :3], eps=1.5, min_samples=8, Lx=box[0], Ly=box[1])
    liquid_pts, vapour_pts = points[liquid], points[~liquid]
    q_vectors, modes_shape, Qxy, Q = _compute_q_vectors(box, normal, alpha)
    pivot = np.sort(get_initial_pivots(liquid_pts, box, normal))
    if len(liquid_pts) < 10 or len(pivot) < 3:
        sys.exit(f"intrinsic fit: no usable liquid cluster ({len(liquid_pts)} liquid atoms, "
                 f"{len(pivot)} pivots) - check the density/temperature knobs or the DBSCAN eps.")
    area = box[0] * box[1]
    tau_ = tau
    modes = None
    for _ in range(Ntries):
        modes = get_surface_modes(liquid_pts[pivot], Qxy, modes_shape)
        new_pivot = np.sort(update_pivots(liquid_pts, q_vectors, modes, pivot, normal, alpha, tau_))
        if new_pivot.shape[0] >= int(ns * area):
            break
        elif new_pivot.shape[0] == pivot.shape[0]:
            tau_ += 0.01
        else:
            pivot = new_pivot
    return q_vectors, modes, liquid_pts, vapour_pts, pivot


def main():
    ap = argparse.ArgumentParser(description="Day-2 slab: intrinsic vs lab-frame density profile.")
    ap.add_argument("--show-surface", action="store_true",
                    help="also save one frame's fitted surface to slab_intrinsic_surface.png")
    ap.add_argument("--start", type=int, default=None,
                    help="first trajectory frame to analyse (default: skip the first quarter)")
    args = ap.parse_args()

    TRAJ = "slab_traj.xyz"
    if not os.path.exists(TRAJ):
        sys.exit(f"{TRAJ} not found - run `lmp_serial -in liquid_vapour.in -var dump 1` first.")
    if not os.path.exists("slab_params.txt"):
        sys.exit("slab_params.txt not found - run liquid_vapour.in first.")

    global DBSCAN                                     # bind the module-level name used by liquid_vapour_dbscan
    try:
        from sklearn.cluster import DBSCAN
    except ImportError:
        sys.exit("scikit-learn not found - install it (pip install scikit-learn) for the DBSCAN step.")

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    P = read_params("slab_params.txt")
    missing = [k for k in ("Lx", "Ly", "Lz") if k not in P]
    if missing:
        sys.exit(f"slab_params.txt is missing {missing} - rerun liquid_vapour.in to regenerate it.")
    Lx, Ly, Lz = P["Lx"], P["Ly"], P["Lz"]
    box = [Lx, Ly, Lz]
    area = Lx * Ly
    normal, alpha, tau, ns, nbins, Ntries, eps = 2, 0.5, 0.7, 0.8, 100, 100, 5.0

    n_atoms, n_frames = xyz_num_frames(TRAJ)
    start = args.start if args.start is not None else max(1, n_frames // 4)
    if start >= n_frames - 1:
        sys.exit(f"--start {start} leaves fewer than 2 of {n_frames} frames; "
                 f"lower --start or run a longer trajectory.")
    dhist, dhist_int = [], []
    edges = edges_int = None
    last = None
    for t in range(start, n_frames):
        print(f"  frame {t} of {n_frames}", flush=True)
        el, x, y, z = read_frame(TRAJ, t)                       # z is the slab normal (no axis swap)
        points = np.array([x - Lx / 2., y - Ly / 2., z - Lz / 2.]).T
        q_vectors, modes, liquid_pts, vapour_pts, pivot = fit_one_frame(
            points, box, normal, alpha, tau, ns, Ntries)
        sp = surface_from_modes(points[:, 0:2], q_vectors, modes)   # surface elevation under each atom
        meansurf = np.mean(sp)
        # bin BOTH profiles in a per-frame surface-relative coordinate on the SAME fixed
        # range, so every frame contributes to the same bins. Lab frame references the
        # frame MEAN surface (still smeared by capillary waves); intrinsic references the
        # LOCAL surface sp(x,y) (removes the waves). Binning the lab frame on absolute z
        # around a per-frame meansurf, then plotting on the last frame's axis, mis-aligned
        # frames whose mean surface drifts.
        d_lab, edges = np.histogram(points[:, normal] - meansurf, bins=nbins, range=(-eps, eps))
        d_int, edges_int = np.histogram(points[:, normal] - sp, bins=nbins, range=(-eps, eps))
        dhist.append(d_lab)
        dhist_int.append(d_int)
        last = (q_vectors, modes, liquid_pts, vapour_pts, pivot)

    if not dhist:
        sys.exit(f"no frames analysed (start={start} >= n_frames={n_frames}); lower --start.")

    binw = 2.0 * eps / nbins
    centers = 0.5 * (edges[:-1] + edges[1:])                    # shared surface-relative bin centres
    centers_int = 0.5 * (edges_int[:-1] + edges_int[1:])
    rho_lab = np.mean(dhist, axis=0) / (area * binw)            # number density, lab frame
    rho_int = np.mean(dhist_int, axis=0) / (area * binw)        # number density, intrinsic frame

    fig, ax = plt.subplots(figsize=(5.6, 4.0))
    ax.plot(centers, rho_lab, color="#1F3A5F", lw=1.6, label="lab-frame density")
    ax.plot(centers_int, rho_int, color="#B23A2E", lw=1.6, label="intrinsic density")
    ax.set_xlabel(r"distance from the surface $(\sigma)$")
    ax.set_ylabel(r"number density $\rho\ (\sigma^{-3})$")
    ax.set_title("intrinsic vs lab-frame density at the interface", fontsize=10)
    ax.legend(fontsize=8, frameon=False, loc="best")
    fig.tight_layout(); fig.savefig("slab_intrinsic.png", dpi=150)
    print("    plot -> slab_intrinsic.png")

    if args.show_surface and last is not None:
        save_surface_figure(last, box, nbins=60)


def save_surface_figure(fit, box, nbins=60):
    """Save one frame's liquid/vapour/edge scatter + the fitted surface wireframe."""
    import matplotlib.pyplot as plt
    q_vectors, modes, liquid_pts, vapour_pts, pivot = fit
    Lx, Ly = box[0], box[1]
    N = nbins
    X, Y = np.meshgrid(np.linspace(-Lx / 2., Lx / 2., N), np.linspace(-Ly / 2., Ly / 2., N))
    grid = np.array([X.ravel(), Y.ravel(), np.zeros(X.size)]).T
    surf = surface_from_modes(grid, q_vectors, modes).reshape(N, N)
    p = liquid_pts[pivot]
    fig = plt.figure(figsize=(8.0, 4.0))
    ax1 = fig.add_subplot(121)
    ax1.scatter(liquid_pts[:, 1], liquid_pts[:, 2], c="#1F3A5F", s=1.0, label="liquid")
    ax1.scatter(vapour_pts[:, 1], vapour_pts[:, 2], c="#4C9A2A", s=1.0, label="vapour")
    ax1.scatter(p[:, 1], p[:, 2], c="#B23A2E", s=4.0, label="surface atoms")
    ax1.legend(fontsize=7, frameon=False); ax1.set_aspect("equal")
    ax2 = fig.add_subplot(122, projection="3d")
    ax2.scatter(liquid_pts[:, 0], liquid_pts[:, 1], liquid_pts[:, 2], c="#1F3A5F", s=2.0)
    ax2.plot_wireframe(X, Y, surf, lw=0.2, color="#888888")
    msurf = float(np.mean(surf))
    ax2.set_zlim(msurf - 5, msurf + 5)
    fig.tight_layout(); fig.savefig("slab_intrinsic_surface.png", dpi=150)
    print("    plot -> slab_intrinsic_surface.png")


if __name__ == "__main__":
    main()
