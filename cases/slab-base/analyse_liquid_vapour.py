#!/usr/bin/env python3
"""Day 2 - Part 2: liquid-vapour slab density profile and surface tension.

Reads the z number-density profile (slab_density.profile) and, when present, the
binned diagonal stress (slab_stress.profile) written by liquid_vapour.in. It
reports the coexistence densities with a slab-intact guard, forms the surface
tension gamma from the Kirkwood-Buff integral of the pressure tensor across the
two interfaces, and saves rho(z) to slab_density.png and the pressure profile
with its integrand to slab_pressure.png.

By default it reads ONE run from the current folder. Pass --ensemble to average the
shipped reference ensemble in reference/ (reference/output_<id>/ per replica) and
report gamma as a mean +/- standard error; pass --ensemble-mine to average your OWN
ensemble in output_*/ here (from `sbatch ensemble/ensemble.sh`). The shipped
reference in reference/ is read-only and is never touched by a single run or by your
own output_*/, so the two can never contaminate each other.

Run after `lmp_serial -in liquid_vapour.in -var localstress 1`
(then, for the error bar, --ensemble; see ensemble/README.md).
"""
import argparse
import glob
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lammps_io import read_profile, read_stress_profile, read_params

BLUE, RED, GREY, AMBER = "#1F3A5F", "#B23A2E", "#888888", "#C77F1A"
W1090 = np.log(9.0)    # 10-90 width = 2*atanh(0.8)*delta = ln(9)*delta for tanh((u-R)/delta)

# coexistence guard (slab intact vs evaporated); rehearsal-tunable starting values
RHO_LIQ_MIN = 0.35     # the liquid plateau must reach this
RATIO_MIN = 3.0        # rho_liq / rho_vap (a ratio, not an absolute vapour floor)
SEP_MIN = 5.0          # the two slab faces must be this far apart (sigma)


def coexistence(z, rho):
    """Density-based two-phase test (slab intact vs evaporated).

    Smooth rho(z) with a 3-bin moving average; rho_liq = median of the densest
    20% of bins; rho_vap = median of the outer 20%-of-z edge regions (the vapour
    gaps); require rho_liq >= RHO_LIQ_MIN, rho_liq/rho_vap >= RATIO_MIN, and two
    crossings of the mid-density at least SEP_MIN apart. Returns
    (intact, rho_liq, rho_vap, ratio, n_crossings, separation)."""
    order = np.argsort(z)
    z, r = z[order], rho[order]
    rs = np.convolve(np.r_[r[0], r, r[-1]], np.ones(3) / 3.0, mode="valid")
    k = max(3, int(0.2 * len(rs)))
    rho_liq = float(np.median(np.sort(rs)[-k:]))
    span = z.max() - z.min()
    edge = (z < z.min() + 0.2 * span) | (z > z.max() - 0.2 * span)
    rho_vap = float(np.median(rs[edge])) if edge.any() else 0.0
    ratio = rho_liq / rho_vap if rho_vap > 1e-9 else np.inf
    rho_mid = 0.5 * (rho_liq + rho_vap)
    cz = z[np.where(np.diff(np.sign(rs - rho_mid)) != 0)[0]]
    sep = (cz.max() - cz.min()) if len(cz) >= 2 else 0.0
    intact = (rho_liq >= RHO_LIQ_MIN) and (ratio >= RATIO_MIN) and (len(cz) >= 2) and (sep >= SEP_MIN)
    return intact, rho_liq, rho_vap, ratio, len(cz), sep


def _grid_fit(u, r, mid, half, Rrange, drange, n):
    """Least-squares (R, delta) for a folded tanh, by grid search (scipy-free)."""
    best = (np.inf, Rrange[0], drange[0])
    for R in np.linspace(*Rrange, n):
        for d in np.linspace(*drange, n):
            err = float(np.sum((mid - half * np.tanh((u - R) / d) - r) ** 2))
            if err < best[0]:
                best = (err, R, d)
    return best[1], best[2]


def interface_width(z, rho):
    """Fold the slab's two faces onto u=|z-z_c| and fit one tanh ->
    (z_c, R, delta, 10-90 width, rho_l, rho_v). The 10-90 width = ln(9)*delta.

    The plateau/edge/centre estimates use a 3-bin-smoothed profile (robust to
    noise), but the tanh is fitted to the RAW profile: smoothing broadens the
    interface and would bias delta (and the width) high."""
    order = np.argsort(z)
    z, r_raw = z[order], rho[order]
    r = np.convolve(np.r_[r_raw[0], r_raw, r_raw[-1]], np.ones(3) / 3.0, mode="valid")
    k = max(3, int(0.2 * len(r)))
    rho_l = float(np.median(np.sort(r)[-k:]))
    span = z.max() - z.min()
    edge = (z < z.min() + 0.2 * span) | (z > z.max() - 0.2 * span)
    rho_v = float(np.median(r[edge])) if edge.any() else 0.0
    mid, half = 0.5 * (rho_l + rho_v), 0.5 * (rho_l - rho_v)
    cz = z[np.where(np.diff(np.sign(r - mid)) != 0)[0]]
    z_c = 0.5 * (cz.min() + cz.max()) if len(cz) >= 2 else z[np.argmax(r)]
    u = np.abs(z - z_c)
    R, delta = _grid_fit(u, r_raw, mid, half, (0.0, 0.5 * span), (0.2, 6.0), 60)
    R, delta = _grid_fit(u, r_raw, mid, half, (R - 2, R + 2), (max(0.1, delta - 1), delta + 1), 60)
    R, delta = _grid_fit(u, r_raw, mid, half, (R - 0.5, R + 0.5), (max(0.05, delta - 0.3), delta + 0.3), 60)
    return z_c, R, delta, W1090 * delta, rho_l, rho_v


def pressure_profile(S, area, dz):
    """Diagonal pressure tensor per bin from the summed stress S (n_bins, 6).

    Columns of S are [virial_xx,yy,zz, kinetic_xx,yy,zz] summed over each bin
    (norm none). The per-bin pressure is P_aa = -(virial_aa + kinetic_aa)/V_bin
    with V_bin = area*dz. Returns the normal P_N = P_zz and the tangential
    P_T = (P_xx + P_yy)/2 profiles."""
    vbin = area * dz
    Sxx, Syy, Szz = S[:, 0] + S[:, 3], S[:, 1] + S[:, 4], S[:, 2] + S[:, 5]
    P_N = -Szz / vbin
    P_T = -0.5 * (Sxx + Syy) / vbin
    return P_N, P_T


def gamma_from_stress(S, area):
    """Kirkwood-Buff surface tension from the summed stress S (n_bins, 6).

    gamma = (1/2) * integral [P_N(z) - P_T(z)] dz, the 1/2 for the two interfaces.
    With P_aa = -(stress_aa)/V_bin and V_bin = area*dz the dz cancels:
        gamma = (1/(2*area)) * sum_bins [ (S_xx + S_yy)/2 - S_zz ]
    where each S_aa is the virial + kinetic sum for that component."""
    Sxx, Syy, Szz = S[:, 0] + S[:, 3], S[:, 1] + S[:, 4], S[:, 2] + S[:, 5]
    return 0.5 / area * np.sum(0.5 * (Sxx + Syy) - Szz)


def load_run(folder):
    """Read one run folder -> (z, rho, S_or_None, params). S is None if no stress file."""
    dens = os.path.join(folder, "slab_density.profile")
    par = os.path.join(folder, "slab_params.txt")
    if not os.path.exists(dens) or not os.path.exists(par):
        return None
    z, _, rho = read_profile(dens)
    P = read_params(par)
    # drop any bin the chunk grid placed past the box top: bin/1d can add one float
    # round-up bin beyond Lz (LAMMPS `limit ... exact` did not remove it on the test
    # build), so the analyser drops z>=Lz for every run.
    keep = (z < P["Lz"] - 1.0e-8) if "Lz" in P else np.ones(len(z), dtype=bool)
    z, rho = z[keep], rho[keep]
    stress = os.path.join(folder, "slab_stress.profile")
    S = None
    # only accept a stress file when this run actually wrote one. The deck removes a
    # stale slab_stress.profile at start, so a present file is from this run; this
    # gate is the defensive backstop. Default 1 keeps older runs (no localstress key
    # recorded) working, since they only wrote the file when stress was on.
    if os.path.exists(stress) and P.get("localstress", 1) != 0:
        zs, _, S = read_stress_profile(stress)
        zs, S = zs[keep], S[keep]                      # same bins as the density profile
        if not np.allclose(zs, z):
            sys.exit(f"{stress}: z-bins differ from slab_density.profile (stale file?) - rerun this case.")
    return z, rho, S, P


def plot_density(z, rho, out="slab_density.png", title="liquid-vapour slab", fit=None):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("    (matplotlib not found - skipping the plot)")
        return
    fig, ax = plt.subplots(figsize=(5.2, 4.0))
    ax.plot(z, rho, color=GREY, lw=1.1, alpha=0.8, label="profile" if fit else None)
    if fit is not None:
        z_c, R, delta, rho_l, rho_v = fit
        mid, half = 0.5 * (rho_l + rho_v), 0.5 * (rho_l - rho_v)
        zf = np.linspace(z.min(), z.max(), 400)
        ax.plot(zf, mid - half * np.tanh((np.abs(zf - z_c) - R) / delta), color=BLUE, lw=1.6, label="tanh fit")
        for zc in (z_c - R, z_c + R):
            ax.axvline(zc, color=RED, lw=0.7, ls="--")
        ax.legend(fontsize=8, frameon=False, loc="best")
    ax.set_xlabel(r"$z\ (\sigma)$"); ax.set_ylabel(r"number density $\rho(z)\ (\sigma^{-3})$")
    ax.set_title(title, fontsize=10)
    fig.tight_layout(); fig.savefig(out, dpi=150)
    print(f"    plot -> {out}")


def plot_pressure(z, P_N, P_T, out="slab_pressure.png"):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("    (matplotlib not found - skipping the plot)")
        return
    fig, ax = plt.subplots(figsize=(5.2, 4.0))
    ax.plot(z, P_N, color=BLUE, lw=1.4, label=r"$P_N = P_{zz}$")
    ax.plot(z, P_T, color=RED, lw=1.4, label=r"$P_T = (P_{xx}+P_{yy})/2$")
    ax.fill_between(z, P_T, P_N, color=AMBER, alpha=0.25, label=r"$P_N - P_T$ (the interfaces)")
    ax.axhline(0.0, color=GREY, lw=0.8)
    ax.set_xlabel(r"$z\ (\sigma)$"); ax.set_ylabel(r"pressure $(\epsilon/\sigma^3)$")
    ax.set_title("pressure tensor across the slab", fontsize=10)
    ax.legend(fontsize=7, frameon=False, loc="best")
    fig.tight_layout(); fig.savefig(out, dpi=150)
    print(f"    plot -> {out}")


def plot_gamma_convergence(gammas, out="slab_gamma_convergence.png"):
    """Cumulative gamma vs number of replicas averaged - the ensemble payoff."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("    (matplotlib not found - skipping the plot)")
        return
    g = np.asarray(gammas)
    k = np.arange(1, len(g) + 1)
    run = np.cumsum(g) / k
    band = np.array([g[:i + 1].std(ddof=1) / np.sqrt(i + 1) if i >= 1 else 0.0 for i in range(len(g))])
    fig, ax = plt.subplots(figsize=(5.2, 4.0))
    ax.fill_between(k, run - band, run + band, color=GREY, alpha=0.25, label="running standard error")
    ax.plot(k, run, color=BLUE, lw=1.6, label=r"cumulative $\gamma$")
    ax.set_xlabel("number of replicas averaged"); ax.set_ylabel(r"$\gamma\ (\epsilon/\sigma^2)$")
    ax.set_title("surface tension over the ensemble", fontsize=10)
    ax.legend(fontsize=7, frameon=False, loc="best")
    fig.tight_layout(); fig.savefig(out, dpi=150)
    print(f"    plot -> {out}")


def report_coexistence(z, rho):
    intact, rho_liq, rho_vap, ratio, ncross, sep = coexistence(z, rho)
    if not intact:
        print(f"    SLAB EVAPORATED / no two-phase coexistence (rho_liq={rho_liq:.3f}, "
              f"rho_liq/rho_vap={ratio:.1f}, {ncross} crossings, faces {sep:.1f} sigma apart)")
        print("    -> gamma is meaningless at this rcut/T; not reported.")
    else:
        print(f"    coexistence: held (rho_liq={rho_liq:.3f}, rho_vap={rho_vap:.3f}, "
              f"rho_liq/rho_vap={ratio:.1f}, faces {sep:.1f} sigma apart)")
    return intact


def analyse_single():
    run = load_run(".")
    if run is None:
        sys.exit("no slab_density.profile / slab_params.txt here. Run "
                 "`lmp_serial -in liquid_vapour.in -var localstress 1` first, from this folder.")
    z, rho, S, P = run
    T, rcut = P.get("T", float("nan")), P.get("rcut", float("nan"))
    print(f"\n[slab] LIQUID-VAPOUR SLAB  (T*={T:.2f}, rcut={rcut:.2f})")
    intact = report_coexistence(z, rho)
    fit = None
    if intact:                                             # the tanh width is meaningful only for a two-phase slab
        z_c, R, delta, width, rho_l, rho_v = interface_width(z, rho)
        print(f"    10-90 interface width = {width:.2f} sigma")
        fit = (z_c, R, delta, rho_l, rho_v)
    plot_density(z, rho, title=f"liquid-vapour slab (T*={T:.2f}, rcut={rcut:.2f})", fit=fit)
    if S is None:
        print("    (no slab_stress.profile - add `-var localstress 1` to get the surface tension)")
        return
    area = P["Lx"] * P["Ly"]
    dz = float(np.median(np.diff(np.sort(z))))
    g = gamma_from_stress(S, area)
    P_N, P_T = pressure_profile(S, area, dz)
    plot_pressure(z, P_N, P_T)
    if intact:
        if g <= 0:
            print(f"    gamma = {g:.3f} is not physical (an intact slab has gamma > 0); not reported. "
                  f"Check the run is equilibrated and slab_stress.profile is from this run.")
        else:
            print(f"    surface tension gamma = {g:.3f} (LJ units, epsilon/sigma^2) from one run (indicative).")
            print("    -> gamma is a noisy LJ measurement; run the ensemble for a mean +/- error bar.")


def analyse_ensemble(ens_dir="reference", what="ensemble"):
    folders = sorted(glob.glob(os.path.join(ens_dir, "output_*")))
    where = os.path.join(ens_dir, "output_*") if ens_dir != "." else "output_*"   # for guard messages
    runs, bad = [], []
    for f in folders:                                      # reject incomplete replicas loudly, do not silently skip
        r = load_run(f)
        (runs if r is not None else bad).append(r if r is not None else f)
    if bad:
        sys.exit(f"ensemble: incomplete {ens_dir}/output_* folders (missing slab_density.profile or "
                 "slab_params.txt): " + ", ".join(bad) + " - clean and rerun.")
    if not runs:
        if ens_dir == "reference":
            sys.exit("no reference/output_*/ replicas found - the shipped reference ensemble is missing; "
                     "reinstall the package (or regenerate: `sbatch ensemble/ensemble.sh`, then --ensemble-mine).")
        sys.exit("no output_*/ replicas here. Generate your own with `sbatch ensemble/ensemble.sh` first "
                 "(see ensemble/README.md), or drop --ensemble-mine for a single-run analysis.")
    stress_runs = [r for r in runs if r[2] is not None]
    if stress_runs and len(stress_runs) != len(runs):     # density over all replicas but gamma over a subset -> refuse
        sys.exit(f"ensemble: {len(stress_runs)}/{len(runs)} replicas have slab_stress.profile - the "
                 f"density and gamma would come from different replica sets. Clean {where} and rerun all "
                 "replicas with -var localstress 1 (or none, for a density-only ensemble).")
    z0 = runs[0][0]
    P0 = runs[0][3]
    # replicas must share the z grid and the knobs, or a stale/mixed output_* would silently contaminate
    for r in runs[1:]:
        if len(r[0]) != len(z0) or not np.allclose(r[0], z0):
            sys.exit(f"ensemble: replicas have different z grids - clean stale {where} and rerun.")
        for k in ("Lx", "Ly", "Lz", "T", "rcut", "bin", "nequil", "nprod", "dt", "tdamp", "localstress"):
            if (k in P0) != (k in r[3]) or (k in P0 and abs(r[3][k] - P0[k]) > 1e-6):
                sys.exit(f"ensemble: replicas disagree on {k} - mixed/stale {where}; clean and rerun.")
    rho_mean = np.mean([r[1] for r in runs], axis=0)
    T, rcut = P0.get("T", float("nan")), P0.get("rcut", float("nan"))
    print(f"\n[{what}] {len(runs)} replicas ({len(stress_runs)} with stress)  (T*={T:.2f}, rcut={rcut:.2f})")
    intact = report_coexistence(z0, rho_mean)
    fit = None
    if intact:
        z_c, R, delta, width, rho_l, rho_v = interface_width(z0, rho_mean)
        print(f"    10-90 interface width = {width:.2f} sigma")
        fit = (z_c, R, delta, rho_l, rho_v)
    plot_density(z0, rho_mean, title=f"liquid-vapour slab, {len(runs)} replicas (T*={T:.2f})", fit=fit)

    if not stress_runs:
        print("    (no slab_stress.profile in the replicas - rerun the ensemble with -var localstress 1)")
        return
    area = P0["Lx"] * P0["Ly"]
    dz = float(np.median(np.diff(np.sort(z0))))
    g = np.array([gamma_from_stress(r[2], r[3]["Lx"] * r[3]["Ly"]) for r in stress_runs])
    S_mean = np.mean([r[2] for r in stress_runs], axis=0)
    P_N, P_T = pressure_profile(S_mean, area, dz)
    plot_pressure(z0, P_N, P_T)
    if len(g) > 1:
        plot_gamma_convergence(g)
    if intact:
        if g.mean() <= 0:
            print(f"    mean gamma = {g.mean():.3f} is not physical (expected > 0); not reported. "
                  f"Check the replicas are equilibrated and z-normal.")
        elif len(g) > 1:
            sem = g.std(ddof=1) / np.sqrt(len(g))
            print(f"    surface tension gamma = {g.mean():.3f} +/- {sem:.3f} "
                  f"(mean +/- standard error over {len(g)} replicas with stress, LJ units)")
        else:
            print(f"    surface tension gamma = {g.mean():.3f} (one replica with stress, no ensemble "
                  f"error bar - run more replicas)")


def main():
    ap = argparse.ArgumentParser(description="Day-2 L-V slab: density profile + surface tension.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--ensemble", action="store_true",
                   help="average the shipped reference ensemble (reference/output_*) -> gamma + error bar")
    g.add_argument("--ensemble-mine", action="store_true",
                   help="average your OWN ensemble (output_*/ here, from `sbatch ensemble/ensemble.sh`)")
    args = ap.parse_args()
    if args.ensemble_mine:
        analyse_ensemble(".", "your ensemble")
    elif args.ensemble:
        analyse_ensemble("reference", "ensemble")
    else:
        analyse_single()


if __name__ == "__main__":
    main()
