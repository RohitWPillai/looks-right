#!/usr/bin/env python3
# What (cleaned copy: paths changed, analysis unchanged): the pore definition scan ("test B"): each slit-pore run's local viscosity under the 144
#   combinations of five hidden analysis choices, the author's rule per pore width, RESULT.md and eta-by-width.png.
# Who runs it, from this folder:  python3 scan-b.py [--runs-root DIR] [--out DIR]
# Refuses: a runs folder with none of the 21 runs. A missing or unreadable run is listed and left out; a width with
#   fewer than three seeds gets no verdict. It writes only RESULT.md and eta-by-width.png in --out.
import argparse
import itertools
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
COURSE = HERE.parents[1] / "cases" / "pore-base"  # the course's day2-slitpore files as shipped with the pore cases
sys.dont_write_bytecode = True  # the course folder is read only: no __pycache__ there
sys.path[:0] = [str(COURSE), str(COURSE / "poiseuille")]
from analyse_poiseuille import pxz_from_centre, smooth  # noqa: E402  (the course's formulas, imported unchanged)
from lammps_io import read_params, read_vx_rho  # noqa: E402  (the course's readers, imported unchanged)

WIDTHS = (4, 5, 6, 7, 8, 10, 12)  # sigma
SEEDS = (11, 22, 33)
ROUTES = ("parabola", 0.25, 0.5, 1.0)  # the shear rate: a parabola fit, or vx(z) smoothed over this many sigma
MERGES = (1, 2, 4)  # native bins per merged bin
MASKS = ("course", 0.3, 1.0)  # the centreline mask's half-width: the course's rule, or this many sigma
MARGINS = (0.0, 1.0)  # the region: sigma left out next to each inner wall plane (1.0 drops the first adsorbed layer)
STATISTICS = ("median", "mean")
CHOICES = list(itertools.product(ROUTES, MERGES, MASKS, MARGINS, STATISTICS))
DEFAULT = (0.5, 1, "course", 0.0, "median")  # the course's own choices
T95 = 4.303  # t(0.975, 2): the 95% interval of a mean of three seeds
NO_SHEAR = 1e-9  # a shear rate at or below this counts as zero: eta undefined there


def read_runs(root):
    """The scan's runs under root by (width, seed), read with the course's readers, and a line per run left out."""
    runs, missing = {}, []
    for seed in SEEDS:
        for width in WIDTHS:
            label = f"scanb-w{width}-s{seed}-run"
            folder = root / label / "poiseuille"
            profile, params = folder / f"poiseuille_w{width}.profile", folder / f"poiseuille_w{width}.params.txt"
            if not (profile.exists() and params.exists()):
                missing.append(f"{label}: no profile or params file")
                continue
            try:
                runs[width, seed] = read_vx_rho(profile), read_params(params)
            except SystemExit as stop:  # the course's reader stops when no block is complete (a run stopped early)
                missing.append(f"{label}: {stop}")
    return runs, missing


def merged(z, n, vx, rho, factor):
    """Groups of `factor` consecutive bins, a last incomplete group dropped: position and velocity weighted by each
    bin's atom count, mass density a plain mean."""
    groups = len(z) // factor
    z, n, vx, rho = (a[:groups * factor].reshape(groups, factor) for a in (z, n, vx, rho))
    count = n.sum(axis=1)
    return (z * n).sum(axis=1) / count, (vx * n).sum(axis=1) / count, rho.mean(axis=1)


def eta_profile(profile, params, choice):
    """eta(z) = -P_xz(z) / (dvx/dz) of one run under one choice: each region bin's distance from the centreline, and
    eta there (nan outside the window). Merging, then smoothing, then the region cut."""
    route, factor, mask, margin, _ = choice
    z, n, vx, rho = profile
    spacing = factor * (z[-1] - z[0]) / (len(z) - 1)  # the merged spacing, from the profile's z column
    bottom, top, half = params["z_bot_inner"], params["z_top_inner"], 0.5 * params["w_meas"]
    fluid = (n > 0.5) & (z > bottom)  # groups counted from the lower plane; the upper plane is the region cut's
    z, vx, rho = merged(z[fluid], n[fluid], vx[fluid], rho[fluid], factor)
    zc = z - 0.5 * (bottom + top)
    region = (z > bottom + margin) & (z < top - margin)
    if route == "parabola":  # the course's wide-pore route, fitted across the pore (the region cut comes after)
        a, b, _ = np.polyfit(zc, vx, 2)
        dvdz = 2 * a * zc + b
    else:  # the course's narrow-pore route
        dvdz = np.gradient(smooth(vx, max(1, round(route / spacing))), zc)
    pxz = pxz_from_centre(zc, rho, params["gforce"])
    eta = np.full(len(zc), np.nan)
    np.divide(-pxz, dvdz, out=eta, where=np.abs(dvdz) > NO_SHEAR)
    inner = max(2 * spacing, min(0.6, 0.15 * half)) if mask == "course" else mask
    window = (np.abs(zc) >= inner) & (np.abs(zc) < 0.6 * half)
    return zc[region], np.where(window, eta, np.nan)[region]


def answer(eta, statistic):
    """The median or mean of eta(z) over the window; nan (no answer) with fewer than three finite values."""
    values = eta[np.isfinite(eta)]
    if len(values) < 3:
        return math.nan
    return float(np.median(values) if statistic == "median" else np.mean(values))


def judge(answers):
    """the author's rule at one width. answers: each choice's answers at the three seeds (nan: no answer), the default's too.
    Sensitive when a choice's mean is further from the default's mean than the default's 95% half-width, or a choice
    gives no answer; each choice also gets its paired differences (choice minus default, same seed). A default with
    no answer at a seed is itself a no-answer: sensitive, with every move unmeasured (nan)."""
    default = np.array(answers[DEFAULT])
    default_ok = not np.isnan(default).any()
    half_width = T95 * default.std(ddof=1) / math.sqrt(3)
    choices = []
    for choice, values in answers.items():
        if choice == DEFAULT:
            continue
        diffs = np.array(values) - default
        move = diffs.mean()
        no_answer = bool(np.isnan(values).any())  # the choice's own answers, whatever the default's
        paired_half_width = T95 * diffs.std(ddof=1) / math.sqrt(3)
        choices.append({"choice": choice, "mean": np.mean(values), "diffs": diffs, "move": move,
                        "paired_half_width": paired_half_width, "no_answer": no_answer,
                        "moves": no_answer or abs(move) > half_width,
                        "paired_moves": not no_answer and abs(move) > paired_half_width})
    movers = [c["choice"] for c in choices if c["moves"]]
    if not default_ok:
        verdict = "sensitive (the default gives no answer; moves not measured)"
    elif not movers:
        verdict = "no sensitivity detected"
    elif any(c["moves"] and not c["no_answer"] for c in choices):
        verdict = "sensitive"
    else:  # e.g. 4 sigma: the 1.0 sigma mask leaves merged bins too few for an answer (geometry, not the liquid)
        verdict = "sensitive (no answer only)"
    return {"default": default, "default_ok": default_ok, "default_mean": default.mean(), "half_width": half_width,
            "choices": choices, "sensitive": bool(movers) or not default_ok, "verdict": verdict,
            "parabola_alone": bool(movers) and all(c[0] == "parabola" for c in movers)}


INTRO = """# Test B: at which slit-pore widths is a local viscosity defined?

Written by `scan-b.py` from the runs in `{root}`. Each run is
analysed 144 ways: the shear-rate route (a parabola fit, or vx(z) smoothed over 0.25, 0.5 or 1.0 σ) × bins merged by
1, 2 or 4 × the centreline mask (the course's rule, 0.3 or 1.0 σ) × the region (all fluid bins, or less 1.0 σ next to
each wall plane, which drops the first adsorbed layer) × the statistic of eta(z) over the window (median or mean). The
default is the course's own: {default}.

Rule (the author's, fixed before the runs): at a width the result is **sensitive** when any choice's mean over the three seeds differs from the
default's mean by more than the default's 95% half-width (4.303 × the seeds' standard deviation / √3), or the choice
gives no answer (fewer than three finite eta(z) values in the window); otherwise **no sensitivity detected**. When only
no-answers make it sensitive, the verdict reads **sensitive (no answer only)**: a matter of geometry, not of the
liquid (at 4 σ the 1.0 σ mask leaves merged bins too few for an answer). Three
seeds make that half-width wide, so "no sensitivity detected" is weaker than "a local viscosity is defined". The
paired differences (choice minus default, same seed) are the sharper test: the last column counts the choices whose
paired mean difference lies outside its own 95% half-width.
"""
SUMMARY_HEADER = ("| width | seeds | default: mean ± 95% half-width | largest move (its choice) | choices beyond the "
                  "half-width | choices with no answer | verdict | moved by the parabola route alone | paired test: "
                  "choices beyond their own half-width |\n|---|---|---|---|---|---|---|---|---|")
CHOICES_HEADER = ("| choice | mean | move ± its paired half-width | paired differences (s11, s22, s33) | beyond the "
                  "default's half-width | beyond its own half-width |\n|---|---|---|---|---|---|")


def name(choice):
    route, factor, mask, margin, statistic = choice
    route = "parabola fit" if route == "parabola" else f"smoothed {route} σ"
    mask = "course mask" if mask == "course" else f"mask {mask} σ"
    region = "all fluid bins" if margin == 0 else f"less {margin} σ at each plane"
    return f"{route}, bins ×{factor}, {mask}, {region}, {statistic}"


def num(x, sign=""):
    return "no answer" if math.isnan(x) else f"{x:{sign}.3f}"


def yes(flag):
    return "yes" if flag else "no"


def summary_row(width, seeds, result):
    seed_text = f"{len(seeds)} of 3" + (f" ({', '.join(f's{s}' for s in seeds)})" if seeds else "")
    if result is None:
        return f"| {width} σ | {seed_text} | – | – | – | – | no verdict (fewer than three seeds) | – | – |"
    choices = result["choices"]
    answered = [c for c in choices if not c["no_answer"]]
    total = len(choices)
    if not result["default_ok"]:
        return (f"| {width} σ | {seed_text} | no answer (the default fails at a seed) | not measured | not measured "
                f"| {total - len(answered)} of {total} | {result['verdict']} | – | not measured |")
    largest = max(answered, key=lambda c: abs(c["move"]), default=None)
    largest_text = f"{num(largest['move'], '+')} ({name(largest['choice'])})" if largest else "–"
    return (f"| {width} σ | {seed_text} | {num(result['default_mean'])} ± {num(result['half_width'])} | {largest_text} "
            f"| {sum(c['moves'] for c in answered)} of {total} | {total - len(answered)} of {total} | {result['verdict']} "
            f"| {yes(result['parabola_alone'])} | {sum(c['paired_moves'] for c in choices)} of {total} |")


def choice_row(c):
    if c["no_answer"]:
        move = beyond = paired = "no answer"
    elif math.isnan(c["move"]):  # the default has no answer at a seed
        move = beyond = paired = "not measured"
    else:
        move = f"{c['move']:+.3f} ± {c['paired_half_width']:.3f}"
        beyond, paired = yes(c["moves"]), yes(c["paired_moves"])
    return (f"| {name(c['choice'])} | {num(c['mean'])} | {move} | {', '.join(num(d, '+') for d in c['diffs'])} "
            f"| {beyond} | {paired} |")


def report(results, missing, runs_root):
    """RESULT.md: one row per width, then every choice at each width that has a verdict."""
    lines = [INTRO.format(root=runs_root, default=name(DEFAULT)),
             f"Runs read: {21 - len(missing)} of 21. Missing or unreadable runs ({len(missing)}): "
             + ("" if missing else "none."), *[f"- {line}" for line in missing], "", SUMMARY_HEADER]
    lines += [summary_row(width, seeds, result) for width, (seeds, result) in results.items()]
    for width, (seeds, result) in results.items():
        if result is not None:
            defaults = ", ".join(f"s{s} {num(x)}" for s, x in zip(seeds, result["default"]))
            lines += ["", f"## Width {width} σ: every choice", "", f"Default: {defaults}.", "", CHOICES_HEADER]
            lines += [choice_row(c) for c in result["choices"]]
    return "\n".join(lines) + "\n"


def on_grid(grid, zc, eta):
    """eta(z) interpolated onto the grid between its finite values; blank beyond them and across the masked centre."""
    finite = np.isfinite(eta)
    if not finite.any():
        return np.full(len(grid), np.nan)
    values = np.interp(grid, zc[finite], eta[finite], left=np.nan, right=np.nan)
    values[np.abs(grid) < np.abs(zc[finite]).min()] = np.nan
    return values


def figure(runs):
    """eta(z) at each width: the default as a line and the spread of the 144 choices as a band (both means over the
    seeds, on the first seed's native bins), and each seed's default answer as a point on the centreline. One eta
    range for every width, the course's narrow-pore plot's (-6 to 10)."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    widths = [w for w in WIDTHS if any((w, s) in runs for s in SEEDS)]
    fig, axes = plt.subplots(1, len(widths), figsize=(2.4 * len(widths) + 0.6, 3.8), sharey=True, squeeze=False)
    for ax, width in zip(axes[0], widths):
        seeds = [runs[width, s] for s in SEEDS if (width, s) in runs]
        grid = eta_profile(*seeds[0], DEFAULT)[0]
        curves = [np.mean([on_grid(grid, *eta_profile(*run, c)) for run in seeds], axis=0) for c in CHOICES]
        ax.fill_between(grid, np.fmin.reduce(curves), np.fmax.reduce(curves), color="#888888", alpha=0.3,
                        lw=0, label="spread of the 144 choices")
        ax.plot(grid, curves[CHOICES.index(DEFAULT)], color="#1F3A5F", lw=1.6, label="default")
        ax.scatter(np.zeros(len(seeds)), [answer(eta_profile(*run, DEFAULT)[1], "median") for run in seeds],
                   color="#B23A2E", s=14, zorder=3, label="each seed's default answer")
        ax.set_title(f"{width} σ, {len(seeds)} of 3 seeds", fontsize=9)
        ax.set_xlabel("z from the centreline (σ)", fontsize=8)
    axes[0][0].set_ylim(-6, 10)
    axes[0][0].set_ylabel("eta(z)")
    fig.legend(*axes[0][0].get_legend_handles_labels(), loc="lower center", ncol=3, fontsize=8, frameon=False)
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    return fig


def main(argv=None):
    parser = argparse.ArgumentParser(description="Test B: the definition scan of the slit-pore runs.")
    parser.add_argument("--runs-root", type=Path, default=HERE / "runs")
    parser.add_argument("--out", type=Path, default=HERE)
    args = parser.parse_args(argv)
    runs, missing = read_runs(args.runs_root)
    if not runs:
        sys.exit(f"no scan-b runs under {args.runs_root}")
    results = {}
    for width in WIDTHS:
        seeds = [s for s in SEEDS if (width, s) in runs]
        if len(seeds) == 3:
            answers = {c: [answer(eta_profile(*runs[width, s], c)[1], c[4]) for s in seeds] for c in CHOICES}
            results[width] = seeds, judge(answers)
        else:  # every width gets a row: fewer than three seeds, no verdict
            results[width] = seeds, None
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "RESULT.md").write_text(report(results, missing, "runs/"))
    figure(runs).savefig(args.out / "eta-by-width.png", dpi=150)
    print(f"wrote RESULT.md and eta-by-width.png in {args.out}; runs missing or unreadable: {len(missing)} of 21")


if __name__ == "__main__":
    main()
