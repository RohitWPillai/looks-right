# Test B: at which slit-pore widths is a local viscosity defined?

Written by `scan-b.py` from the runs in `runs/`. Each run is
analysed 144 ways: the shear-rate route (a parabola fit, or vx(z) smoothed over 0.25, 0.5 or 1.0 σ) × bins merged by
1, 2 or 4 × the centreline mask (the course's rule, 0.3 or 1.0 σ) × the region (all fluid bins, or less 1.0 σ next to
each wall plane, which drops the first adsorbed layer) × the statistic of eta(z) over the window (median or mean). The
default is the course's own: smoothed 0.5 σ, bins ×1, course mask, all fluid bins, median.

Rule (the author's, fixed before the runs): at a width the result is **sensitive** when any choice's mean over the three seeds differs from the
default's mean by more than the default's 95% half-width (4.303 × the seeds' standard deviation / √3), or the choice
gives no answer (fewer than three finite eta(z) values in the window); otherwise **no sensitivity detected**. When only
no-answers make it sensitive, the verdict reads **sensitive (no answer only)**: a matter of geometry, not of the
liquid (at 4 σ the 1.0 σ mask leaves merged bins too few for an answer). Three
seeds make that half-width wide, so "no sensitivity detected" is weaker than "a local viscosity is defined". The
paired differences (choice minus default, same seed) are the sharper test: the last column counts the choices whose
paired mean difference lies outside its own 95% half-width.

Runs read: 21 of 21. Missing or unreadable runs (0): none.

| width | seeds | default: mean ± 95% half-width | largest move (its choice) | choices beyond the half-width | choices with no answer | verdict | moved by the parabola route alone | paired test: choices beyond their own half-width |
|---|---|---|---|---|---|---|---|---|
| 4 σ | 3 of 3 (s11, s22, s33) | 2.192 ± 0.542 | +14.862 (smoothed 1.0 σ, bins ×1, mask 1.0 σ, all fluid bins, mean) | 36 of 143 | 48 of 143 | sensitive | no | 29 of 143 |
| 5 σ | 3 of 3 (s11, s22, s33) | 2.676 ± 0.582 | +2.944 (smoothed 0.5 σ, bins ×1, mask 1.0 σ, all fluid bins, mean) | 40 of 143 | 16 of 143 | sensitive | no | 32 of 143 |
| 6 σ | 3 of 3 (s11, s22, s33) | 2.772 ± 0.845 | -0.640 (smoothed 0.25 σ, bins ×4, course mask, all fluid bins, median) | 0 of 143 | 0 of 143 | no sensitivity detected | no | 20 of 143 |
| 7 σ | 3 of 3 (s11, s22, s33) | 2.372 ± 0.420 | +3.781 (smoothed 0.25 σ, bins ×1, mask 1.0 σ, all fluid bins, mean) | 14 of 143 | 0 of 143 | sensitive | no | 42 of 143 |
| 8 σ | 3 of 3 (s11, s22, s33) | 2.429 ± 0.233 | +0.571 (smoothed 0.25 σ, bins ×1, mask 0.3 σ, all fluid bins, mean) | 12 of 143 | 0 of 143 | sensitive | no | 12 of 143 |
| 10 σ | 3 of 3 (s11, s22, s33) | 2.462 ± 0.062 | +0.490 (smoothed 0.25 σ, bins ×1, mask 0.3 σ, all fluid bins, mean) | 46 of 143 | 0 of 143 | sensitive | no | 14 of 143 |
| 12 σ | 3 of 3 (s11, s22, s33) | 2.421 ± 0.168 | +0.587 (smoothed 0.25 σ, bins ×1, course mask, all fluid bins, mean) | 6 of 143 | 0 of 143 | sensitive | no | 0 of 143 |

## Width 4 σ: every choice

Default: s11 2.235, s22 2.385, s33 1.955.

| choice | mean | move ± its paired half-width | paired differences (s11, s22, s33) | beyond the default's half-width | beyond its own half-width |
|---|---|---|---|---|---|
| parabola fit, bins ×1, course mask, all fluid bins, median | 1.949 | -0.243 ± 0.549 | -0.294, -0.434, -0.002 | no | no |
| parabola fit, bins ×1, course mask, all fluid bins, mean | 2.022 | -0.170 ± 0.553 | -0.238, -0.351, +0.079 | no | no |
| parabola fit, bins ×1, course mask, less 1.0 σ at each plane, median | 1.890 | -0.302 ± 0.545 | -0.378, -0.473, -0.054 | no | no |
| parabola fit, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.002 | -0.190 ± 0.555 | -0.258, -0.371, +0.060 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, all fluid bins, median | 1.949 | -0.243 ± 0.549 | -0.294, -0.434, -0.002 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.022 | -0.170 ± 0.553 | -0.238, -0.351, +0.079 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 1.890 | -0.302 ± 0.545 | -0.378, -0.473, -0.054 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.002 | -0.190 ± 0.555 | -0.258, -0.371, +0.060 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, all fluid bins, median | 2.091 | -0.101 ± 0.548 | -0.167, -0.281, +0.145 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.091 | -0.101 ± 0.548 | -0.167, -0.281, +0.145 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| parabola fit, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| parabola fit, bins ×2, course mask, all fluid bins, median | 1.978 | -0.213 ± 0.416 | -0.229, -0.372, -0.039 | no | no |
| parabola fit, bins ×2, course mask, all fluid bins, mean | 1.988 | -0.204 ± 0.420 | -0.221, -0.363, -0.026 | no | no |
| parabola fit, bins ×2, course mask, less 1.0 σ at each plane, median | 1.867 | -0.325 ± 0.498 | -0.356, -0.508, -0.110 | no | no |
| parabola fit, bins ×2, course mask, less 1.0 σ at each plane, mean | 1.945 | -0.247 ± 0.424 | -0.265, -0.407, -0.068 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, all fluid bins, median | 1.978 | -0.213 ± 0.416 | -0.229, -0.372, -0.039 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, all fluid bins, mean | 1.988 | -0.204 ± 0.420 | -0.221, -0.363, -0.026 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 1.867 | -0.325 ± 0.498 | -0.356, -0.508, -0.110 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 1.945 | -0.247 ± 0.424 | -0.265, -0.407, -0.068 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, all fluid bins, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| parabola fit, bins ×2, mask 1.0 σ, all fluid bins, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| parabola fit, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| parabola fit, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| parabola fit, bins ×4, course mask, all fluid bins, median | 2.225 | +0.033 ± 0.514 | -0.082, -0.092, +0.272 | no | no |
| parabola fit, bins ×4, course mask, all fluid bins, mean | 2.222 | +0.030 ± 0.507 | -0.083, -0.092, +0.266 | no | no |
| parabola fit, bins ×4, course mask, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| parabola fit, bins ×4, course mask, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| parabola fit, bins ×4, mask 0.3 σ, all fluid bins, median | 2.302 | +0.110 ± 0.506 | -0.005, -0.010, +0.345 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.319 | +0.127 ± 0.511 | +0.010, +0.006, +0.364 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.307 | +0.115 ± 0.448 | +0.011, +0.010, +0.323 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.327 | +0.135 ± 0.513 | +0.018, +0.014, +0.373 | no | no |
| parabola fit, bins ×4, mask 1.0 σ, all fluid bins, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| parabola fit, bins ×4, mask 1.0 σ, all fluid bins, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| parabola fit, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| parabola fit, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.25 σ, bins ×1, course mask, all fluid bins, median | 1.836 | -0.356 ± 0.814 | -0.720, -0.086, -0.261 | no | no |
| smoothed 0.25 σ, bins ×1, course mask, all fluid bins, mean | 5.922 | +3.730 ± 12.321 | -1.211, +3.694, +8.708 | yes | no |
| smoothed 0.25 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 2.331 | +0.139 ± 1.541 | -0.567, +0.597, +0.387 | no | no |
| smoothed 0.25 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 7.229 | +5.037 ± 15.814 | -1.328, +5.034, +11.403 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 1.836 | -0.356 ± 0.814 | -0.720, -0.086, -0.261 | no | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 5.922 | +3.730 ± 12.321 | -1.211, +3.694, +8.708 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.331 | +0.139 ± 1.541 | -0.567, +0.597, +0.387 | no | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 7.229 | +5.037 ± 15.814 | -1.328, +5.034, +11.403 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 1.367 | -0.825 ± 0.319 | -0.772, -0.971, -0.731 | yes | yes |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 1.350 | -0.842 ± 0.350 | -0.800, -0.999, -0.727 | yes | yes |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.25 σ, bins ×2, course mask, all fluid bins, median | 2.745 | +0.553 ± 1.782 | +0.040, +0.247, +1.373 | yes | no |
| smoothed 0.25 σ, bins ×2, course mask, all fluid bins, mean | 9.650 | +7.458 ± 28.468 | +0.882, +0.802, +20.689 | yes | no |
| smoothed 0.25 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 3.371 | +1.179 ± 2.291 | +0.158, +1.429, +1.951 | yes | no |
| smoothed 0.25 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 12.440 | +10.248 ± 37.876 | +1.463, +1.428, +27.853 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.745 | +0.553 ± 1.782 | +0.040, +0.247, +1.373 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 9.650 | +7.458 ± 28.468 | +0.882, +0.802, +20.689 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 3.371 | +1.179 ± 2.291 | +0.158, +1.429, +1.951 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 12.440 | +10.248 ± 37.876 | +1.463, +1.428, +27.853 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, all fluid bins, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.25 σ, bins ×4, course mask, all fluid bins, median | 1.882 | -0.310 ± 0.442 | -0.400, -0.424, -0.104 | no | no |
| smoothed 0.25 σ, bins ×4, course mask, all fluid bins, mean | 1.890 | -0.302 ± 0.403 | -0.382, -0.408, -0.115 | no | no |
| smoothed 0.25 σ, bins ×4, course mask, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.25 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 1.944 | -0.248 ± 0.316 | -0.291, -0.348, -0.104 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.070 | -0.122 ± 0.302 | -0.033, -0.261, -0.073 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.122 | -0.070 ± 0.404 | +0.107, -0.213, -0.104 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.145 | -0.047 ± 0.394 | +0.111, -0.206, -0.047 | no | no |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, all fluid bins, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.5 σ, bins ×1, course mask, all fluid bins, mean | 2.661 | +0.469 ± 0.469 | +0.283, +0.464, +0.660 | no | yes |
| smoothed 0.5 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 2.640 | +0.448 ± 0.088 | +0.481, +0.453, +0.410 | no | yes |
| smoothed 0.5 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.938 | +0.746 ± 0.522 | +0.529, +0.759, +0.949 | yes | yes |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 2.192 | +0.000 ± 0.000 | +0.000, +0.000, +0.000 | no | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.661 | +0.469 ± 0.469 | +0.283, +0.464, +0.660 | no | yes |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.640 | +0.448 ± 0.088 | +0.481, +0.453, +0.410 | no | yes |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.938 | +0.746 ± 0.522 | +0.529, +0.759, +0.949 | yes | yes |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 1.697 | -0.495 ± 0.235 | -0.577, -0.516, -0.391 | no | yes |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 1.692 | -0.500 ± 0.321 | -0.578, -0.571, -0.351 | no | yes |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.5 σ, bins ×2, course mask, all fluid bins, median | 2.835 | +0.643 ± 0.422 | +0.476, +0.637, +0.815 | yes | yes |
| smoothed 0.5 σ, bins ×2, course mask, all fluid bins, mean | 2.731 | +0.539 ± 0.725 | +0.349, +0.392, +0.875 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.914 | +0.722 ± 0.923 | +0.400, +0.637, +1.128 | yes | no |
| smoothed 0.5 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.699 | +0.507 ± 0.919 | +0.242, +0.348, +0.929 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.835 | +0.643 ± 0.422 | +0.476, +0.637, +0.815 | yes | yes |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.731 | +0.539 ± 0.725 | +0.349, +0.392, +0.875 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.914 | +0.722 ± 0.923 | +0.400, +0.637, +1.128 | yes | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.699 | +0.507 ± 0.919 | +0.242, +0.348, +0.929 | no | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, all fluid bins, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.5 σ, bins ×4, course mask, all fluid bins, median | 1.882 | -0.310 ± 0.442 | -0.400, -0.424, -0.104 | no | no |
| smoothed 0.5 σ, bins ×4, course mask, all fluid bins, mean | 1.890 | -0.302 ± 0.403 | -0.382, -0.408, -0.115 | no | no |
| smoothed 0.5 σ, bins ×4, course mask, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.5 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 1.944 | -0.248 ± 0.316 | -0.291, -0.348, -0.104 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.070 | -0.122 ± 0.302 | -0.033, -0.261, -0.073 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.122 | -0.070 ± 0.404 | +0.107, -0.213, -0.104 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.145 | -0.047 ± 0.394 | +0.111, -0.206, -0.047 | no | no |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, all fluid bins, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 1.0 σ, bins ×1, course mask, all fluid bins, median | 3.021 | +0.829 ± 0.394 | +0.677, +0.817, +0.994 | yes | yes |
| smoothed 1.0 σ, bins ×1, course mask, all fluid bins, mean | 5.781 | +3.589 ± 3.138 | +2.765, +5.043, +2.959 | yes | yes |
| smoothed 1.0 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 2.337 | +0.145 ± 0.472 | +0.000, +0.076, +0.360 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.560 | +0.368 ± 0.463 | +0.337, +0.199, +0.568 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 3.021 | +0.829 ± 0.394 | +0.677, +0.817, +0.994 | yes | yes |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 5.781 | +3.589 ± 3.138 | +2.765, +5.043, +2.959 | yes | yes |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.337 | +0.145 ± 0.472 | +0.000, +0.076, +0.360 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.560 | +0.368 ± 0.463 | +0.337, +0.199, +0.568 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 13.047 | +10.855 ± 2.365 | +10.033, +10.634, +11.898 | yes | yes |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 17.054 | +14.862 ± 15.350 | +11.263, +21.997, +11.327 | yes | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 1.0 σ, bins ×2, course mask, all fluid bins, median | 2.766 | +0.574 ± 0.271 | +0.562, +0.472, +0.689 | yes | yes |
| smoothed 1.0 σ, bins ×2, course mask, all fluid bins, mean | 4.803 | +2.611 ± 1.100 | +2.395, +2.319, +3.120 | yes | yes |
| smoothed 1.0 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.689 | +0.497 ± 0.291 | +0.513, +0.372, +0.605 | no | yes |
| smoothed 1.0 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.530 | +0.338 ± 0.414 | +0.289, +0.202, +0.524 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.766 | +0.574 ± 0.271 | +0.562, +0.472, +0.689 | yes | yes |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 4.803 | +2.611 ± 1.100 | +2.395, +2.319, +3.120 | yes | yes |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.689 | +0.497 ± 0.291 | +0.513, +0.372, +0.605 | no | yes |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.530 | +0.338 ± 0.414 | +0.289, +0.202, +0.524 | no | no |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, all fluid bins, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 1.0 σ, bins ×4, course mask, all fluid bins, median | 10.237 | +8.045 ± 4.894 | +6.221, +7.779, +10.134 | yes | yes |
| smoothed 1.0 σ, bins ×4, course mask, all fluid bins, mean | 11.423 | +9.231 ± 8.302 | +6.500, +8.236, +12.958 | yes | yes |
| smoothed 1.0 σ, bins ×4, course mask, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 1.0 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 6.103 | +3.911 ± 1.504 | +3.377, +3.786, +4.569 | yes | yes |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 8.639 | +6.447 ± 5.790 | +4.554, +5.736, +9.050 | yes | yes |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 4.515 | +2.323 ± 0.974 | +1.994, +2.218, +2.757 | yes | yes |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 4.586 | +2.394 ± 1.133 | +2.019, +2.261, +2.902 | yes | yes |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, all fluid bins, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |

## Width 5 σ: every choice

Default: s11 2.435, s22 2.902, s33 2.690.

| choice | mean | move ± its paired half-width | paired differences (s11, s22, s33) | beyond the default's half-width | beyond its own half-width |
|---|---|---|---|---|---|
| parabola fit, bins ×1, course mask, all fluid bins, median | 2.582 | -0.093 ± 0.282 | +0.037, -0.163, -0.154 | no | no |
| parabola fit, bins ×1, course mask, all fluid bins, mean | 2.596 | -0.080 ± 0.293 | +0.055, -0.137, -0.160 | no | no |
| parabola fit, bins ×1, course mask, less 1.0 σ at each plane, median | 2.582 | -0.093 ± 0.282 | +0.037, -0.163, -0.154 | no | no |
| parabola fit, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.596 | -0.080 ± 0.293 | +0.055, -0.137, -0.160 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, all fluid bins, median | 2.553 | -0.123 ± 0.296 | +0.015, -0.182, -0.200 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.573 | -0.103 ± 0.295 | +0.034, -0.161, -0.181 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.553 | -0.123 ± 0.296 | +0.015, -0.182, -0.200 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.573 | -0.103 ± 0.295 | +0.034, -0.161, -0.181 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, all fluid bins, median | 2.452 | -0.224 ± 0.297 | -0.086, -0.293, -0.292 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.495 | -0.181 ± 0.302 | -0.041, -0.243, -0.258 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.452 | -0.224 ± 0.297 | -0.086, -0.293, -0.292 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.495 | -0.181 ± 0.302 | -0.041, -0.243, -0.258 | no | no |
| parabola fit, bins ×2, course mask, all fluid bins, median | 2.578 | -0.098 ± 0.311 | +0.046, -0.162, -0.179 | no | no |
| parabola fit, bins ×2, course mask, all fluid bins, mean | 2.604 | -0.072 ± 0.310 | +0.072, -0.147, -0.141 | no | no |
| parabola fit, bins ×2, course mask, less 1.0 σ at each plane, median | 2.578 | -0.098 ± 0.311 | +0.046, -0.162, -0.179 | no | no |
| parabola fit, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.604 | -0.072 ± 0.310 | +0.072, -0.147, -0.141 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, all fluid bins, median | 2.578 | -0.098 ± 0.311 | +0.046, -0.162, -0.179 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.604 | -0.072 ± 0.310 | +0.072, -0.147, -0.141 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.578 | -0.098 ± 0.311 | +0.046, -0.162, -0.179 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.604 | -0.072 ± 0.310 | +0.072, -0.147, -0.141 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, all fluid bins, median | 2.473 | -0.202 ± 0.321 | -0.053, -0.282, -0.271 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.476 | -0.200 ± 0.321 | -0.051, -0.282, -0.268 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.473 | -0.202 ± 0.321 | -0.053, -0.282, -0.271 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.476 | -0.200 ± 0.321 | -0.051, -0.282, -0.268 | no | no |
| parabola fit, bins ×4, course mask, all fluid bins, median | 2.830 | +0.154 ± 0.284 | +0.282, +0.062, +0.120 | no | no |
| parabola fit, bins ×4, course mask, all fluid bins, mean | 2.797 | +0.121 ± 0.275 | +0.248, +0.047, +0.068 | no | no |
| parabola fit, bins ×4, course mask, less 1.0 σ at each plane, median | 2.830 | +0.154 ± 0.284 | +0.282, +0.062, +0.120 | no | no |
| parabola fit, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.797 | +0.121 ± 0.275 | +0.248, +0.047, +0.068 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, all fluid bins, median | 2.822 | +0.147 ± 0.262 | +0.267, +0.069, +0.104 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.816 | +0.140 ± 0.274 | +0.264, +0.053, +0.102 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.822 | +0.147 ± 0.262 | +0.267, +0.069, +0.104 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.816 | +0.140 ± 0.274 | +0.264, +0.053, +0.102 | no | no |
| parabola fit, bins ×4, mask 1.0 σ, all fluid bins, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| parabola fit, bins ×4, mask 1.0 σ, all fluid bins, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| parabola fit, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| parabola fit, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.25 σ, bins ×1, course mask, all fluid bins, median | 1.872 | -0.804 ± 0.310 | -0.664, -0.846, -0.902 | yes | yes |
| smoothed 0.25 σ, bins ×1, course mask, all fluid bins, mean | 1.097 | -1.579 ± 5.138 | -0.405, -3.967, -0.366 | yes | no |
| smoothed 0.25 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 1.872 | -0.804 ± 0.310 | -0.664, -0.846, -0.902 | yes | yes |
| smoothed 0.25 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 1.097 | -1.579 ± 5.138 | -0.405, -3.967, -0.366 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 1.894 | -0.781 ± 0.159 | -0.718, -0.846, -0.780 | yes | yes |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | -0.005 | -2.681 ± 6.112 | -4.268, -3.929, +0.153 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 1.894 | -0.781 ± 0.159 | -0.718, -0.846, -0.780 | yes | yes |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | -0.005 | -2.681 ± 6.112 | -4.268, -3.929, +0.153 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 2.943 | +0.267 ± 3.006 | +1.589, -0.003, -0.786 | no | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | -0.096 | -2.772 ± 10.242 | +0.023, -7.507, -0.832 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.943 | +0.267 ± 3.006 | +1.589, -0.003, -0.786 | no | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | -0.096 | -2.772 ± 10.242 | +0.023, -7.507, -0.832 | yes | no |
| smoothed 0.25 σ, bins ×2, course mask, all fluid bins, median | 2.715 | +0.039 ± 1.164 | -0.385, -0.040, +0.542 | no | no |
| smoothed 0.25 σ, bins ×2, course mask, all fluid bins, mean | 3.560 | +0.884 ± 15.790 | -5.517, +0.975, +7.194 | yes | no |
| smoothed 0.25 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.715 | +0.039 ± 1.164 | -0.385, -0.040, +0.542 | no | no |
| smoothed 0.25 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 3.560 | +0.884 ± 15.790 | -5.517, +0.975, +7.194 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.715 | +0.039 ± 1.164 | -0.385, -0.040, +0.542 | no | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 3.560 | +0.884 ± 15.790 | -5.517, +0.975, +7.194 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.715 | +0.039 ± 1.164 | -0.385, -0.040, +0.542 | no | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 3.560 | +0.884 ± 15.790 | -5.517, +0.975, +7.194 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, all fluid bins, median | 4.135 | +1.459 ± 3.281 | +0.361, +1.093, +2.925 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | -0.128 | -2.804 ± 28.867 | -16.088, +2.201, +5.474 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 4.135 | +1.459 ± 3.281 | +0.361, +1.093, +2.925 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | -0.128 | -2.804 ± 28.867 | -16.088, +2.201, +5.474 | yes | no |
| smoothed 0.25 σ, bins ×4, course mask, all fluid bins, median | 2.576 | -0.100 ± 0.319 | +0.045, -0.146, -0.200 | no | no |
| smoothed 0.25 σ, bins ×4, course mask, all fluid bins, mean | 2.600 | -0.076 ± 0.547 | +0.177, -0.176, -0.227 | no | no |
| smoothed 0.25 σ, bins ×4, course mask, less 1.0 σ at each plane, median | 2.576 | -0.100 ± 0.319 | +0.045, -0.146, -0.200 | no | no |
| smoothed 0.25 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.600 | -0.076 ± 0.547 | +0.177, -0.176, -0.227 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 2.417 | -0.258 ± 0.238 | -0.274, -0.346, -0.156 | no | yes |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.551 | -0.125 ± 0.706 | -0.229, -0.342, +0.197 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.417 | -0.258 ± 0.238 | -0.274, -0.346, -0.156 | no | yes |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.551 | -0.125 ± 0.706 | -0.229, -0.342, +0.197 | no | no |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, all fluid bins, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.5 σ, bins ×1, course mask, all fluid bins, mean | 3.756 | +1.081 ± 0.928 | +1.418, +0.679, +1.145 | yes | yes |
| smoothed 0.5 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 2.676 | +0.000 ± 0.000 | +0.000, +0.000, +0.000 | no | no |
| smoothed 0.5 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 3.756 | +1.081 ± 0.928 | +1.418, +0.679, +1.145 | yes | yes |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 2.602 | -0.074 ± 0.615 | +0.128, +0.000, -0.350 | no | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 3.337 | +0.661 ± 1.750 | +1.474, +0.257, +0.252 | yes | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.602 | -0.074 ± 0.615 | +0.128, +0.000, -0.350 | no | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 3.337 | +0.661 ± 1.750 | +1.474, +0.257, +0.252 | yes | no |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 5.025 | +2.349 ± 2.342 | +2.173, +1.507, +3.368 | yes | yes |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 5.620 | +2.944 ± 2.040 | +3.820, +2.192, +2.819 | yes | yes |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 5.025 | +2.349 ± 2.342 | +2.173, +1.507, +3.368 | yes | yes |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 5.620 | +2.944 ± 2.040 | +3.820, +2.192, +2.819 | yes | yes |
| smoothed 0.5 σ, bins ×2, course mask, all fluid bins, median | 2.676 | -0.000 ± 0.261 | -0.119, +0.038, +0.081 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, all fluid bins, mean | 3.063 | +0.387 ± 0.718 | +0.286, +0.162, +0.713 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.676 | -0.000 ± 0.261 | -0.119, +0.038, +0.081 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 3.063 | +0.387 ± 0.718 | +0.286, +0.162, +0.713 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.676 | -0.000 ± 0.261 | -0.119, +0.038, +0.081 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 3.063 | +0.387 ± 0.718 | +0.286, +0.162, +0.713 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.676 | -0.000 ± 0.261 | -0.119, +0.038, +0.081 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 3.063 | +0.387 ± 0.718 | +0.286, +0.162, +0.713 | no | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, all fluid bins, median | 3.361 | +0.685 ± 0.800 | +1.030, +0.392, +0.633 | yes | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | 3.479 | +0.803 ± 0.990 | +1.263, +0.577, +0.569 | yes | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 3.361 | +0.685 ± 0.800 | +1.030, +0.392, +0.633 | yes | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 3.479 | +0.803 ± 0.990 | +1.263, +0.577, +0.569 | yes | no |
| smoothed 0.5 σ, bins ×4, course mask, all fluid bins, median | 2.576 | -0.100 ± 0.319 | +0.045, -0.146, -0.200 | no | no |
| smoothed 0.5 σ, bins ×4, course mask, all fluid bins, mean | 2.600 | -0.076 ± 0.547 | +0.177, -0.176, -0.227 | no | no |
| smoothed 0.5 σ, bins ×4, course mask, less 1.0 σ at each plane, median | 2.576 | -0.100 ± 0.319 | +0.045, -0.146, -0.200 | no | no |
| smoothed 0.5 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.600 | -0.076 ± 0.547 | +0.177, -0.176, -0.227 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 2.417 | -0.258 ± 0.238 | -0.274, -0.346, -0.156 | no | yes |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.551 | -0.125 ± 0.706 | -0.229, -0.342, +0.197 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.417 | -0.258 ± 0.238 | -0.274, -0.346, -0.156 | no | yes |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.551 | -0.125 ± 0.706 | -0.229, -0.342, +0.197 | no | no |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, all fluid bins, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 1.0 σ, bins ×1, course mask, all fluid bins, median | 2.862 | +0.187 ± 0.188 | +0.146, +0.140, +0.274 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, all fluid bins, mean | 3.005 | +0.329 ± 0.299 | +0.282, +0.239, +0.466 | no | yes |
| smoothed 1.0 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 2.862 | +0.187 ± 0.188 | +0.146, +0.140, +0.274 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 3.005 | +0.329 ± 0.299 | +0.282, +0.239, +0.466 | no | yes |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 2.760 | +0.085 ± 0.064 | +0.107, +0.056, +0.090 | no | yes |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.889 | +0.213 ± 0.288 | +0.176, +0.120, +0.343 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.760 | +0.085 ± 0.064 | +0.107, +0.056, +0.090 | no | yes |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.889 | +0.213 ± 0.288 | +0.176, +0.120, +0.343 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 2.591 | -0.085 ± 0.487 | +0.132, -0.138, -0.249 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.842 | +0.166 ± 0.556 | +0.394, +0.157, -0.053 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.591 | -0.085 ± 0.487 | +0.132, -0.138, -0.249 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.842 | +0.166 ± 0.556 | +0.394, +0.157, -0.053 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, all fluid bins, median | 2.788 | +0.112 ± 0.286 | +0.239, +0.015, +0.081 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, all fluid bins, mean | 2.919 | +0.243 ± 0.169 | +0.258, +0.168, +0.302 | no | yes |
| smoothed 1.0 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.788 | +0.112 ± 0.286 | +0.239, +0.015, +0.081 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.919 | +0.243 ± 0.169 | +0.258, +0.168, +0.302 | no | yes |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.788 | +0.112 ± 0.286 | +0.239, +0.015, +0.081 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.919 | +0.243 ± 0.169 | +0.258, +0.168, +0.302 | no | yes |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.788 | +0.112 ± 0.286 | +0.239, +0.015, +0.081 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.919 | +0.243 ± 0.169 | +0.258, +0.168, +0.302 | no | yes |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, all fluid bins, median | 3.283 | +0.607 ± 0.430 | +0.795, +0.573, +0.454 | yes | yes |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | 3.355 | +0.679 ± 0.540 | +0.897, +0.678, +0.463 | yes | yes |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 3.283 | +0.607 ± 0.430 | +0.795, +0.573, +0.454 | yes | yes |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 3.355 | +0.679 ± 0.540 | +0.897, +0.678, +0.463 | yes | yes |
| smoothed 1.0 σ, bins ×4, course mask, all fluid bins, median | 4.417 | +1.741 ± 0.232 | +1.708, +1.669, +1.847 | yes | yes |
| smoothed 1.0 σ, bins ×4, course mask, all fluid bins, mean | 4.672 | +1.996 ± 0.328 | +2.000, +2.126, +1.862 | yes | yes |
| smoothed 1.0 σ, bins ×4, course mask, less 1.0 σ at each plane, median | 4.417 | +1.741 ± 0.232 | +1.708, +1.669, +1.847 | yes | yes |
| smoothed 1.0 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | 4.672 | +1.996 ± 0.328 | +2.000, +2.126, +1.862 | yes | yes |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 2.833 | +0.157 ± 0.192 | +0.128, +0.098, +0.244 | no | no |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 3.553 | +0.877 ± 0.127 | +0.824, +0.880, +0.926 | yes | yes |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.833 | +0.157 ± 0.192 | +0.128, +0.098, +0.244 | no | no |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 3.553 | +0.877 ± 0.127 | +0.824, +0.880, +0.926 | yes | yes |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, all fluid bins, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | no answer | no answer | no answer, no answer, no answer | no answer | no answer |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | no answer | no answer | no answer, no answer, no answer | no answer | no answer |

## Width 6 σ: every choice

Default: s11 2.385, s22 3.024, s33 2.908.

| choice | mean | move ± its paired half-width | paired differences (s11, s22, s33) | beyond the default's half-width | beyond its own half-width |
|---|---|---|---|---|---|
| parabola fit, bins ×1, course mask, all fluid bins, median | 2.418 | -0.355 ± 0.736 | -0.016, -0.562, -0.486 | no | no |
| parabola fit, bins ×1, course mask, all fluid bins, mean | 2.421 | -0.351 ± 0.745 | -0.008, -0.566, -0.479 | no | no |
| parabola fit, bins ×1, course mask, less 1.0 σ at each plane, median | 2.418 | -0.355 ± 0.736 | -0.016, -0.562, -0.486 | no | no |
| parabola fit, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.421 | -0.351 ± 0.745 | -0.008, -0.566, -0.479 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, all fluid bins, median | 2.433 | -0.339 ± 0.757 | +0.008, -0.562, -0.463 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.442 | -0.330 ± 0.743 | +0.011, -0.543, -0.459 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.433 | -0.339 ± 0.757 | +0.008, -0.562, -0.463 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.442 | -0.330 ± 0.743 | +0.011, -0.543, -0.459 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, all fluid bins, median | 2.453 | -0.320 ± 0.755 | +0.027, -0.542, -0.443 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.450 | -0.322 ± 0.746 | +0.021, -0.538, -0.449 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.453 | -0.320 ± 0.755 | +0.027, -0.542, -0.443 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.450 | -0.322 ± 0.746 | +0.021, -0.538, -0.449 | no | no |
| parabola fit, bins ×2, course mask, all fluid bins, median | 2.405 | -0.368 ± 0.703 | -0.043, -0.560, -0.500 | no | no |
| parabola fit, bins ×2, course mask, all fluid bins, mean | 2.417 | -0.355 ± 0.713 | -0.026, -0.555, -0.483 | no | no |
| parabola fit, bins ×2, course mask, less 1.0 σ at each plane, median | 2.405 | -0.368 ± 0.703 | -0.043, -0.560, -0.500 | no | no |
| parabola fit, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.417 | -0.355 ± 0.713 | -0.026, -0.555, -0.483 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, all fluid bins, median | 2.405 | -0.368 ± 0.703 | -0.043, -0.560, -0.500 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.417 | -0.355 ± 0.713 | -0.026, -0.555, -0.483 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.405 | -0.368 ± 0.703 | -0.043, -0.560, -0.500 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.417 | -0.355 ± 0.713 | -0.026, -0.555, -0.483 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, all fluid bins, median | 2.441 | -0.331 ± 0.719 | -0.000, -0.537, -0.457 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.434 | -0.339 ± 0.714 | -0.010, -0.540, -0.466 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.441 | -0.331 ± 0.719 | -0.000, -0.537, -0.457 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.434 | -0.339 ± 0.714 | -0.010, -0.540, -0.466 | no | no |
| parabola fit, bins ×4, course mask, all fluid bins, median | 2.512 | -0.261 ± 0.733 | +0.077, -0.469, -0.390 | no | no |
| parabola fit, bins ×4, course mask, all fluid bins, mean | 2.509 | -0.263 ± 0.740 | +0.077, -0.477, -0.390 | no | no |
| parabola fit, bins ×4, course mask, less 1.0 σ at each plane, median | 2.512 | -0.261 ± 0.733 | +0.077, -0.469, -0.390 | no | no |
| parabola fit, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.509 | -0.263 ± 0.740 | +0.077, -0.477, -0.390 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, all fluid bins, median | 2.501 | -0.272 ± 0.720 | +0.061, -0.469, -0.406 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.500 | -0.272 ± 0.739 | +0.068, -0.485, -0.399 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.501 | -0.272 ± 0.720 | +0.061, -0.469, -0.406 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.500 | -0.272 ± 0.739 | +0.068, -0.485, -0.399 | no | no |
| parabola fit, bins ×4, mask 1.0 σ, all fluid bins, median | 2.512 | -0.261 ± 0.733 | +0.077, -0.469, -0.390 | no | no |
| parabola fit, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.509 | -0.263 ± 0.740 | +0.077, -0.477, -0.390 | no | no |
| parabola fit, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.512 | -0.261 ± 0.733 | +0.077, -0.469, -0.390 | no | no |
| parabola fit, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.509 | -0.263 ± 0.740 | +0.077, -0.477, -0.390 | no | no |
| smoothed 0.25 σ, bins ×1, course mask, all fluid bins, median | 3.018 | +0.245 ± 0.420 | +0.178, +0.120, +0.438 | no | no |
| smoothed 0.25 σ, bins ×1, course mask, all fluid bins, mean | 2.524 | -0.249 ± 6.345 | +1.654, -3.151, +0.751 | no | no |
| smoothed 0.25 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 3.018 | +0.245 ± 0.420 | +0.178, +0.120, +0.438 | no | no |
| smoothed 0.25 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.524 | -0.249 ± 6.345 | +1.654, -3.151, +0.751 | no | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 2.705 | -0.068 ± 0.580 | +0.024, -0.333, +0.106 | no | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.494 | -0.279 ± 5.901 | +1.607, -2.947, +0.504 | no | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.705 | -0.068 ± 0.580 | +0.024, -0.333, +0.106 | no | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.494 | -0.279 ± 5.901 | +1.607, -2.947, +0.504 | no | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 2.404 | -0.368 ± 0.637 | -0.304, -0.651, -0.151 | no | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 3.345 | +0.572 ± 3.113 | +2.013, -0.263, -0.033 | no | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.404 | -0.368 ± 0.637 | -0.304, -0.651, -0.151 | no | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 3.345 | +0.572 ± 3.113 | +2.013, -0.263, -0.033 | no | no |
| smoothed 0.25 σ, bins ×2, course mask, all fluid bins, median | 2.565 | -0.207 ± 0.366 | -0.095, -0.152, -0.374 | no | no |
| smoothed 0.25 σ, bins ×2, course mask, all fluid bins, mean | 3.071 | +0.299 ± 0.416 | +0.483, +0.255, +0.157 | no | no |
| smoothed 0.25 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.565 | -0.207 ± 0.366 | -0.095, -0.152, -0.374 | no | no |
| smoothed 0.25 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 3.071 | +0.299 ± 0.416 | +0.483, +0.255, +0.157 | no | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.565 | -0.207 ± 0.366 | -0.095, -0.152, -0.374 | no | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 3.071 | +0.299 ± 0.416 | +0.483, +0.255, +0.157 | no | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.565 | -0.207 ± 0.366 | -0.095, -0.152, -0.374 | no | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 3.071 | +0.299 ± 0.416 | +0.483, +0.255, +0.157 | no | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, all fluid bins, median | 2.263 | -0.509 ± 0.567 | -0.247, -0.661, -0.619 | no | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.766 | -0.006 ± 1.467 | +0.659, -0.467, -0.211 | no | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.263 | -0.509 ± 0.567 | -0.247, -0.661, -0.619 | no | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.766 | -0.006 ± 1.467 | +0.659, -0.467, -0.211 | no | no |
| smoothed 0.25 σ, bins ×4, course mask, all fluid bins, median | 2.132 | -0.640 ± 0.555 | -0.406, -0.850, -0.664 | no | yes |
| smoothed 0.25 σ, bins ×4, course mask, all fluid bins, mean | 2.141 | -0.631 ± 0.614 | -0.356, -0.834, -0.703 | no | yes |
| smoothed 0.25 σ, bins ×4, course mask, less 1.0 σ at each plane, median | 2.132 | -0.640 ± 0.555 | -0.406, -0.850, -0.664 | no | yes |
| smoothed 0.25 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.141 | -0.631 ± 0.614 | -0.356, -0.834, -0.703 | no | yes |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 2.268 | -0.504 ± 0.709 | -0.177, -0.700, -0.636 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.318 | -0.455 ± 0.565 | -0.198, -0.632, -0.534 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.268 | -0.504 ± 0.709 | -0.177, -0.700, -0.636 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.318 | -0.455 ± 0.565 | -0.198, -0.632, -0.534 | no | no |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, all fluid bins, median | 2.132 | -0.640 ± 0.555 | -0.406, -0.850, -0.664 | no | yes |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.141 | -0.631 ± 0.614 | -0.356, -0.834, -0.703 | no | yes |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.132 | -0.640 ± 0.555 | -0.406, -0.850, -0.664 | no | yes |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.141 | -0.631 ± 0.614 | -0.356, -0.834, -0.703 | no | yes |
| smoothed 0.5 σ, bins ×1, course mask, all fluid bins, mean | 3.182 | +0.410 ± 0.402 | +0.397, +0.578, +0.255 | no | yes |
| smoothed 0.5 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 2.772 | +0.000 ± 0.000 | +0.000, +0.000, +0.000 | no | no |
| smoothed 0.5 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 3.182 | +0.410 ± 0.402 | +0.397, +0.578, +0.255 | no | yes |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 2.582 | -0.191 ± 0.351 | -0.028, -0.267, -0.277 | no | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 3.001 | +0.228 ± 0.403 | +0.297, +0.345, +0.043 | no | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.582 | -0.191 ± 0.351 | -0.028, -0.267, -0.277 | no | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 3.001 | +0.228 ± 0.403 | +0.297, +0.345, +0.043 | no | no |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 2.351 | -0.421 ± 0.396 | -0.254, -0.572, -0.437 | no | yes |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.733 | -0.039 ± 1.110 | +0.444, -0.437, -0.125 | no | no |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.351 | -0.421 ± 0.396 | -0.254, -0.572, -0.437 | no | yes |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.733 | -0.039 ± 1.110 | +0.444, -0.437, -0.125 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, all fluid bins, median | 2.579 | -0.193 ± 0.223 | -0.101, -0.199, -0.280 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, all fluid bins, mean | 2.602 | -0.170 ± 0.550 | +0.085, -0.296, -0.300 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.579 | -0.193 ± 0.223 | -0.101, -0.199, -0.280 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.602 | -0.170 ± 0.550 | +0.085, -0.296, -0.300 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.579 | -0.193 ± 0.223 | -0.101, -0.199, -0.280 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.602 | -0.170 ± 0.550 | +0.085, -0.296, -0.300 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.579 | -0.193 ± 0.223 | -0.101, -0.199, -0.280 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.602 | -0.170 ± 0.550 | +0.085, -0.296, -0.300 | no | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, all fluid bins, median | 2.409 | -0.364 ± 0.713 | -0.040, -0.588, -0.462 | no | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.531 | -0.241 ± 0.889 | +0.162, -0.524, -0.361 | no | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.409 | -0.364 ± 0.713 | -0.040, -0.588, -0.462 | no | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.531 | -0.241 ± 0.889 | +0.162, -0.524, -0.361 | no | no |
| smoothed 0.5 σ, bins ×4, course mask, all fluid bins, median | 2.132 | -0.640 ± 0.555 | -0.406, -0.850, -0.664 | no | yes |
| smoothed 0.5 σ, bins ×4, course mask, all fluid bins, mean | 2.141 | -0.631 ± 0.614 | -0.356, -0.834, -0.703 | no | yes |
| smoothed 0.5 σ, bins ×4, course mask, less 1.0 σ at each plane, median | 2.132 | -0.640 ± 0.555 | -0.406, -0.850, -0.664 | no | yes |
| smoothed 0.5 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.141 | -0.631 ± 0.614 | -0.356, -0.834, -0.703 | no | yes |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 2.268 | -0.504 ± 0.709 | -0.177, -0.700, -0.636 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.318 | -0.455 ± 0.565 | -0.198, -0.632, -0.534 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.268 | -0.504 ± 0.709 | -0.177, -0.700, -0.636 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.318 | -0.455 ± 0.565 | -0.198, -0.632, -0.534 | no | no |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, all fluid bins, median | 2.132 | -0.640 ± 0.555 | -0.406, -0.850, -0.664 | no | yes |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.141 | -0.631 ± 0.614 | -0.356, -0.834, -0.703 | no | yes |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.132 | -0.640 ± 0.555 | -0.406, -0.850, -0.664 | no | yes |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.141 | -0.631 ± 0.614 | -0.356, -0.834, -0.703 | no | yes |
| smoothed 1.0 σ, bins ×1, course mask, all fluid bins, median | 2.443 | -0.329 ± 0.527 | -0.084, -0.454, -0.449 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, all fluid bins, mean | 2.431 | -0.341 ± 0.625 | -0.056, -0.529, -0.439 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 2.443 | -0.329 ± 0.527 | -0.084, -0.454, -0.449 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.431 | -0.341 ± 0.625 | -0.056, -0.529, -0.439 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 2.472 | -0.301 ± 0.468 | -0.084, -0.429, -0.388 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.499 | -0.274 ± 0.672 | +0.038, -0.451, -0.407 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.472 | -0.301 ± 0.468 | -0.084, -0.429, -0.388 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.499 | -0.274 ± 0.672 | +0.038, -0.451, -0.407 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 2.557 | -0.215 ± 0.603 | +0.057, -0.409, -0.293 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.538 | -0.235 ± 0.740 | +0.101, -0.466, -0.339 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.557 | -0.215 ± 0.603 | +0.057, -0.409, -0.293 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.538 | -0.235 ± 0.740 | +0.101, -0.466, -0.339 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, all fluid bins, median | 2.447 | -0.325 ± 0.588 | -0.052, -0.473, -0.451 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, all fluid bins, mean | 2.462 | -0.310 ± 0.613 | -0.027, -0.475, -0.429 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.447 | -0.325 ± 0.588 | -0.052, -0.473, -0.451 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.462 | -0.310 ± 0.613 | -0.027, -0.475, -0.429 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.447 | -0.325 ± 0.588 | -0.052, -0.473, -0.451 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.462 | -0.310 ± 0.613 | -0.027, -0.475, -0.429 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.447 | -0.325 ± 0.588 | -0.052, -0.473, -0.451 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.462 | -0.310 ± 0.613 | -0.027, -0.475, -0.429 | no | no |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, all fluid bins, median | 2.543 | -0.230 ± 0.742 | +0.110, -0.450, -0.349 | no | no |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.514 | -0.258 ± 0.731 | +0.075, -0.482, -0.367 | no | no |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.543 | -0.230 ± 0.742 | +0.110, -0.450, -0.349 | no | no |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.514 | -0.258 ± 0.731 | +0.075, -0.482, -0.367 | no | no |
| smoothed 1.0 σ, bins ×4, course mask, all fluid bins, median | 2.378 | -0.395 ± 0.674 | -0.085, -0.589, -0.510 | no | no |
| smoothed 1.0 σ, bins ×4, course mask, all fluid bins, mean | 2.384 | -0.388 ± 0.691 | -0.073, -0.602, -0.489 | no | no |
| smoothed 1.0 σ, bins ×4, course mask, less 1.0 σ at each plane, median | 2.378 | -0.395 ± 0.674 | -0.085, -0.589, -0.510 | no | no |
| smoothed 1.0 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.384 | -0.388 ± 0.691 | -0.073, -0.602, -0.489 | no | no |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 2.427 | -0.345 ± 0.577 | -0.082, -0.520, -0.435 | no | no |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.410 | -0.363 ± 0.629 | -0.074, -0.545, -0.469 | no | no |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.427 | -0.345 ± 0.577 | -0.082, -0.520, -0.435 | no | no |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.410 | -0.363 ± 0.629 | -0.074, -0.545, -0.469 | no | no |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, all fluid bins, median | 2.378 | -0.395 ± 0.674 | -0.085, -0.589, -0.510 | no | no |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.384 | -0.388 ± 0.691 | -0.073, -0.602, -0.489 | no | no |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.378 | -0.395 ± 0.674 | -0.085, -0.589, -0.510 | no | no |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.384 | -0.388 ± 0.691 | -0.073, -0.602, -0.489 | no | no |

## Width 7 σ: every choice

Default: s11 2.412, s22 2.517, s33 2.186.

| choice | mean | move ± its paired half-width | paired differences (s11, s22, s33) | beyond the default's half-width | beyond its own half-width |
|---|---|---|---|---|---|
| parabola fit, bins ×1, course mask, all fluid bins, median | 2.588 | +0.216 ± 0.234 | +0.171, +0.152, +0.324 | no | no |
| parabola fit, bins ×1, course mask, all fluid bins, mean | 2.578 | +0.206 ± 0.239 | +0.165, +0.138, +0.316 | no | no |
| parabola fit, bins ×1, course mask, less 1.0 σ at each plane, median | 2.588 | +0.216 ± 0.234 | +0.171, +0.152, +0.324 | no | no |
| parabola fit, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.578 | +0.206 ± 0.239 | +0.165, +0.138, +0.316 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, all fluid bins, median | 2.575 | +0.203 ± 0.223 | +0.158, +0.145, +0.307 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.568 | +0.196 ± 0.239 | +0.155, +0.128, +0.307 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.575 | +0.203 ± 0.223 | +0.158, +0.145, +0.307 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.568 | +0.196 ± 0.239 | +0.155, +0.128, +0.307 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, all fluid bins, median | 2.582 | +0.210 ± 0.228 | +0.170, +0.145, +0.315 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.574 | +0.202 ± 0.239 | +0.160, +0.133, +0.312 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.582 | +0.210 ± 0.228 | +0.170, +0.145, +0.315 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.574 | +0.202 ± 0.239 | +0.160, +0.133, +0.312 | no | no |
| parabola fit, bins ×2, course mask, all fluid bins, median | 2.587 | +0.215 ± 0.232 | +0.176, +0.148, +0.322 | no | no |
| parabola fit, bins ×2, course mask, all fluid bins, mean | 2.582 | +0.210 ± 0.232 | +0.171, +0.142, +0.316 | no | no |
| parabola fit, bins ×2, course mask, less 1.0 σ at each plane, median | 2.587 | +0.215 ± 0.232 | +0.176, +0.148, +0.322 | no | no |
| parabola fit, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.582 | +0.210 ± 0.232 | +0.171, +0.142, +0.316 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, all fluid bins, median | 2.567 | +0.196 ± 0.201 | +0.158, +0.140, +0.288 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.573 | +0.201 ± 0.232 | +0.163, +0.133, +0.308 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.567 | +0.196 ± 0.201 | +0.158, +0.140, +0.288 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.573 | +0.201 ± 0.232 | +0.163, +0.133, +0.308 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, all fluid bins, median | 2.560 | +0.189 ± 0.217 | +0.150, +0.127, +0.288 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.570 | +0.199 ± 0.233 | +0.160, +0.130, +0.305 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.560 | +0.189 ± 0.217 | +0.150, +0.127, +0.288 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.570 | +0.199 ± 0.233 | +0.160, +0.130, +0.305 | no | no |
| parabola fit, bins ×4, course mask, all fluid bins, median | 2.631 | +0.259 ± 0.227 | +0.224, +0.191, +0.363 | no | yes |
| parabola fit, bins ×4, course mask, all fluid bins, mean | 2.629 | +0.258 ± 0.219 | +0.231, +0.186, +0.356 | no | yes |
| parabola fit, bins ×4, course mask, less 1.0 σ at each plane, median | 2.631 | +0.259 ± 0.227 | +0.224, +0.191, +0.363 | no | yes |
| parabola fit, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.629 | +0.258 ± 0.219 | +0.231, +0.186, +0.356 | no | yes |
| parabola fit, bins ×4, mask 0.3 σ, all fluid bins, median | 2.634 | +0.262 ± 0.224 | +0.231, +0.191, +0.363 | no | yes |
| parabola fit, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.631 | +0.260 ± 0.219 | +0.234, +0.187, +0.358 | no | yes |
| parabola fit, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.634 | +0.262 ± 0.224 | +0.231, +0.191, +0.363 | no | yes |
| parabola fit, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.631 | +0.260 ± 0.219 | +0.234, +0.187, +0.358 | no | yes |
| parabola fit, bins ×4, mask 1.0 σ, all fluid bins, median | 2.631 | +0.259 ± 0.227 | +0.216, +0.196, +0.364 | no | yes |
| parabola fit, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.627 | +0.255 ± 0.220 | +0.223, +0.187, +0.355 | no | yes |
| parabola fit, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.631 | +0.259 ± 0.227 | +0.216, +0.196, +0.364 | no | yes |
| parabola fit, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.627 | +0.255 ± 0.220 | +0.223, +0.187, +0.355 | no | yes |
| smoothed 0.25 σ, bins ×1, course mask, all fluid bins, median | 2.279 | -0.093 ± 0.261 | -0.042, -0.024, -0.214 | no | no |
| smoothed 0.25 σ, bins ×1, course mask, all fluid bins, mean | 4.694 | +2.323 ± 8.877 | +0.371, +0.150, +6.446 | yes | no |
| smoothed 0.25 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 2.279 | -0.093 ± 0.261 | -0.042, -0.024, -0.214 | no | no |
| smoothed 0.25 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 4.694 | +2.323 ± 8.877 | +0.371, +0.150, +6.446 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 2.219 | -0.153 ± 0.146 | -0.097, -0.147, -0.214 | no | yes |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 3.406 | +1.034 ± 9.896 | -1.831, -0.650, +5.583 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.219 | -0.153 ± 0.146 | -0.097, -0.147, -0.214 | no | yes |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 3.406 | +1.034 ± 9.896 | -1.831, -0.650, +5.583 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 2.512 | +0.140 ± 0.578 | +0.176, +0.353, -0.108 | no | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 6.153 | +3.781 ± 12.509 | +0.646, +1.109, +9.589 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.512 | +0.140 ± 0.578 | +0.176, +0.353, -0.108 | no | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 6.153 | +3.781 ± 12.509 | +0.646, +1.109, +9.589 | yes | no |
| smoothed 0.25 σ, bins ×2, course mask, all fluid bins, median | 2.395 | +0.024 ± 0.519 | +0.036, +0.226, -0.191 | no | no |
| smoothed 0.25 σ, bins ×2, course mask, all fluid bins, mean | 2.730 | +0.358 ± 0.542 | +0.124, +0.394, +0.556 | no | no |
| smoothed 0.25 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.395 | +0.024 ± 0.519 | +0.036, +0.226, -0.191 | no | no |
| smoothed 0.25 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.730 | +0.358 ± 0.542 | +0.124, +0.394, +0.556 | no | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.307 | -0.065 ± 0.288 | +0.036, -0.040, -0.191 | no | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 3.134 | +0.762 ± 3.869 | +0.242, -0.468, +2.513 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.307 | -0.065 ± 0.288 | +0.036, -0.040, -0.191 | no | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 3.134 | +0.762 ± 3.869 | +0.242, -0.468, +2.513 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, all fluid bins, median | 2.711 | +0.340 ± 0.446 | +0.354, +0.512, +0.154 | no | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | 3.029 | +0.657 ± 0.815 | +0.374, +0.579, +1.017 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.711 | +0.340 ± 0.446 | +0.354, +0.512, +0.154 | no | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 3.029 | +0.657 ± 0.815 | +0.374, +0.579, +1.017 | yes | no |
| smoothed 0.25 σ, bins ×4, course mask, all fluid bins, median | 2.493 | +0.122 ± 0.316 | +0.093, +0.011, +0.261 | no | no |
| smoothed 0.25 σ, bins ×4, course mask, all fluid bins, mean | 2.468 | +0.096 ± 0.196 | +0.071, +0.033, +0.185 | no | no |
| smoothed 0.25 σ, bins ×4, course mask, less 1.0 σ at each plane, median | 2.493 | +0.122 ± 0.316 | +0.093, +0.011, +0.261 | no | no |
| smoothed 0.25 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.468 | +0.096 ± 0.196 | +0.071, +0.033, +0.185 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 2.386 | +0.014 ± 0.410 | +0.093, -0.175, +0.125 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.414 | +0.042 ± 0.189 | +0.066, -0.043, +0.103 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.386 | +0.014 ± 0.410 | +0.093, -0.175, +0.125 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.414 | +0.042 ± 0.189 | +0.066, -0.043, +0.103 | no | no |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, all fluid bins, median | 2.455 | +0.083 ± 0.362 | +0.139, -0.082, +0.193 | no | no |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.447 | +0.075 ± 0.339 | +0.136, -0.082, +0.170 | no | no |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.455 | +0.083 ± 0.362 | +0.139, -0.082, +0.193 | no | no |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.447 | +0.075 ± 0.339 | +0.136, -0.082, +0.170 | no | no |
| smoothed 0.5 σ, bins ×1, course mask, all fluid bins, mean | 2.603 | +0.231 ± 0.244 | +0.124, +0.316, +0.253 | no | no |
| smoothed 0.5 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 2.372 | +0.000 ± 0.000 | +0.000, +0.000, +0.000 | no | no |
| smoothed 0.5 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.603 | +0.231 ± 0.244 | +0.124, +0.316, +0.253 | no | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 2.394 | +0.022 ± 0.065 | +0.016, +0.051, +0.000 | no | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 3.204 | +0.833 ± 0.653 | +1.136, +0.679, +0.683 | yes | yes |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.394 | +0.022 ± 0.065 | +0.016, +0.051, +0.000 | no | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 3.204 | +0.833 ± 0.653 | +1.136, +0.679, +0.683 | yes | yes |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 2.618 | +0.246 ± 0.271 | +0.201, +0.166, +0.370 | no | no |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.794 | +0.423 ± 0.263 | +0.300, +0.476, +0.491 | yes | yes |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.618 | +0.246 ± 0.271 | +0.201, +0.166, +0.370 | no | no |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.794 | +0.423 ± 0.263 | +0.300, +0.476, +0.491 | yes | yes |
| smoothed 0.5 σ, bins ×2, course mask, all fluid bins, median | 2.482 | +0.110 ± 0.235 | +0.019, +0.209, +0.103 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, all fluid bins, mean | 2.500 | +0.129 ± 0.168 | +0.064, +0.122, +0.199 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.482 | +0.110 ± 0.235 | +0.019, +0.209, +0.103 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.500 | +0.129 ± 0.168 | +0.064, +0.122, +0.199 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.512 | +0.140 ± 0.148 | +0.108, +0.209, +0.103 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.605 | +0.233 ± 0.126 | +0.241, +0.179, +0.280 | no | yes |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.512 | +0.140 ± 0.148 | +0.108, +0.209, +0.103 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.605 | +0.233 ± 0.126 | +0.241, +0.179, +0.280 | no | yes |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, all fluid bins, median | 2.599 | +0.227 ± 0.110 | +0.181, +0.269, +0.232 | no | yes |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.617 | +0.245 ± 0.136 | +0.208, +0.220, +0.308 | no | yes |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.599 | +0.227 ± 0.110 | +0.181, +0.269, +0.232 | no | yes |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.617 | +0.245 ± 0.136 | +0.208, +0.220, +0.308 | no | yes |
| smoothed 0.5 σ, bins ×4, course mask, all fluid bins, median | 2.493 | +0.122 ± 0.316 | +0.093, +0.011, +0.261 | no | no |
| smoothed 0.5 σ, bins ×4, course mask, all fluid bins, mean | 2.468 | +0.096 ± 0.196 | +0.071, +0.033, +0.185 | no | no |
| smoothed 0.5 σ, bins ×4, course mask, less 1.0 σ at each plane, median | 2.493 | +0.122 ± 0.316 | +0.093, +0.011, +0.261 | no | no |
| smoothed 0.5 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.468 | +0.096 ± 0.196 | +0.071, +0.033, +0.185 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 2.386 | +0.014 ± 0.410 | +0.093, -0.175, +0.125 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.414 | +0.042 ± 0.189 | +0.066, -0.043, +0.103 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.386 | +0.014 ± 0.410 | +0.093, -0.175, +0.125 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.414 | +0.042 ± 0.189 | +0.066, -0.043, +0.103 | no | no |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, all fluid bins, median | 2.455 | +0.083 ± 0.362 | +0.139, -0.082, +0.193 | no | no |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.447 | +0.075 ± 0.339 | +0.136, -0.082, +0.170 | no | no |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.455 | +0.083 ± 0.362 | +0.139, -0.082, +0.193 | no | no |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.447 | +0.075 ± 0.339 | +0.136, -0.082, +0.170 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, all fluid bins, median | 2.554 | +0.183 ± 0.245 | +0.132, +0.119, +0.296 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, all fluid bins, mean | 2.597 | +0.225 ± 0.162 | +0.183, +0.191, +0.300 | no | yes |
| smoothed 1.0 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 2.554 | +0.183 ± 0.245 | +0.132, +0.119, +0.296 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.597 | +0.225 ± 0.162 | +0.183, +0.191, +0.300 | no | yes |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 2.506 | +0.134 ± 0.267 | +0.091, +0.055, +0.256 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.556 | +0.184 ± 0.196 | +0.147, +0.131, +0.275 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.506 | +0.134 ± 0.267 | +0.091, +0.055, +0.256 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.556 | +0.184 ± 0.196 | +0.147, +0.131, +0.275 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 2.576 | +0.204 ± 0.164 | +0.227, +0.130, +0.256 | no | yes |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.609 | +0.238 ± 0.152 | +0.201, +0.203, +0.308 | no | yes |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.576 | +0.204 ± 0.164 | +0.227, +0.130, +0.256 | no | yes |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.609 | +0.238 ± 0.152 | +0.201, +0.203, +0.308 | no | yes |
| smoothed 1.0 σ, bins ×2, course mask, all fluid bins, median | 2.514 | +0.142 ± 0.176 | +0.101, +0.101, +0.224 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, all fluid bins, mean | 2.540 | +0.168 ± 0.164 | +0.134, +0.126, +0.245 | no | yes |
| smoothed 1.0 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.514 | +0.142 ± 0.176 | +0.101, +0.101, +0.224 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.540 | +0.168 ± 0.164 | +0.134, +0.126, +0.245 | no | yes |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.473 | +0.102 ± 0.281 | +0.103, -0.012, +0.214 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.525 | +0.153 ± 0.170 | +0.157, +0.083, +0.220 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.473 | +0.102 ± 0.281 | +0.103, -0.012, +0.214 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.525 | +0.153 ± 0.170 | +0.157, +0.083, +0.220 | no | no |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, all fluid bins, median | 2.553 | +0.182 ± 0.079 | +0.145, +0.202, +0.198 | no | yes |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.569 | +0.197 ± 0.158 | +0.176, +0.148, +0.269 | no | yes |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.553 | +0.182 ± 0.079 | +0.145, +0.202, +0.198 | no | yes |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.569 | +0.197 ± 0.158 | +0.176, +0.148, +0.269 | no | yes |
| smoothed 1.0 σ, bins ×4, course mask, all fluid bins, median | 2.530 | +0.159 ± 0.167 | +0.129, +0.111, +0.236 | no | no |
| smoothed 1.0 σ, bins ×4, course mask, all fluid bins, mean | 2.715 | +0.344 ± 0.159 | +0.338, +0.283, +0.410 | no | yes |
| smoothed 1.0 σ, bins ×4, course mask, less 1.0 σ at each plane, median | 2.530 | +0.159 ± 0.167 | +0.129, +0.111, +0.236 | no | no |
| smoothed 1.0 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.715 | +0.344 ± 0.159 | +0.338, +0.283, +0.410 | no | yes |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 2.482 | +0.110 ± 0.248 | +0.118, +0.007, +0.206 | no | no |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.653 | +0.281 ± 0.184 | +0.275, +0.210, +0.358 | no | yes |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.482 | +0.110 ± 0.248 | +0.118, +0.007, +0.206 | no | no |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.653 | +0.281 ± 0.184 | +0.275, +0.210, +0.358 | no | yes |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, all fluid bins, median | 2.506 | +0.134 ± 0.196 | +0.163, +0.045, +0.194 | no | no |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.736 | +0.364 ± 0.186 | +0.389, +0.280, +0.423 | no | yes |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.506 | +0.134 ± 0.196 | +0.163, +0.045, +0.194 | no | no |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.736 | +0.364 ± 0.186 | +0.389, +0.280, +0.423 | no | yes |

## Width 8 σ: every choice

Default: s11 2.532, s22 2.347, s33 2.407.

| choice | mean | move ± its paired half-width | paired differences (s11, s22, s33) | beyond the default's half-width | beyond its own half-width |
|---|---|---|---|---|---|
| parabola fit, bins ×1, course mask, all fluid bins, median | 2.493 | +0.064 ± 0.218 | -0.025, +0.151, +0.066 | no | no |
| parabola fit, bins ×1, course mask, all fluid bins, mean | 2.495 | +0.066 ± 0.218 | -0.023, +0.153, +0.070 | no | no |
| parabola fit, bins ×1, course mask, less 1.0 σ at each plane, median | 2.493 | +0.064 ± 0.218 | -0.025, +0.151, +0.066 | no | no |
| parabola fit, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.495 | +0.066 ± 0.218 | -0.023, +0.153, +0.070 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, all fluid bins, median | 2.498 | +0.069 ± 0.215 | -0.022, +0.151, +0.078 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.502 | +0.073 ± 0.219 | -0.016, +0.160, +0.076 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.498 | +0.069 ± 0.215 | -0.022, +0.151, +0.078 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.502 | +0.073 ± 0.219 | -0.016, +0.160, +0.076 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, all fluid bins, median | 2.500 | +0.071 ± 0.227 | -0.022, +0.161, +0.074 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.499 | +0.071 ± 0.218 | -0.019, +0.157, +0.074 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.500 | +0.071 ± 0.227 | -0.022, +0.161, +0.074 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.499 | +0.071 ± 0.218 | -0.019, +0.157, +0.074 | no | no |
| parabola fit, bins ×2, course mask, all fluid bins, median | 2.493 | +0.064 ± 0.244 | -0.034, +0.163, +0.064 | no | no |
| parabola fit, bins ×2, course mask, all fluid bins, mean | 2.497 | +0.068 ± 0.219 | -0.023, +0.154, +0.073 | no | no |
| parabola fit, bins ×2, course mask, less 1.0 σ at each plane, median | 2.493 | +0.064 ± 0.244 | -0.034, +0.163, +0.064 | no | no |
| parabola fit, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.497 | +0.068 ± 0.219 | -0.023, +0.154, +0.073 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, all fluid bins, median | 2.498 | +0.069 ± 0.235 | -0.026, +0.163, +0.071 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.502 | +0.073 ± 0.219 | -0.018, +0.159, +0.078 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.498 | +0.069 ± 0.235 | -0.026, +0.163, +0.071 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.502 | +0.073 ± 0.219 | -0.018, +0.159, +0.078 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, all fluid bins, median | 2.496 | +0.067 ± 0.236 | -0.026, +0.163, +0.064 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.500 | +0.072 ± 0.219 | -0.019, +0.157, +0.077 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.496 | +0.067 ± 0.236 | -0.026, +0.163, +0.064 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.500 | +0.072 ± 0.219 | -0.019, +0.157, +0.077 | no | no |
| parabola fit, bins ×4, course mask, all fluid bins, median | 2.542 | +0.114 ± 0.217 | +0.024, +0.199, +0.118 | no | no |
| parabola fit, bins ×4, course mask, all fluid bins, mean | 2.540 | +0.112 ± 0.216 | +0.022, +0.197, +0.116 | no | no |
| parabola fit, bins ×4, course mask, less 1.0 σ at each plane, median | 2.542 | +0.114 ± 0.217 | +0.024, +0.199, +0.118 | no | no |
| parabola fit, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.540 | +0.112 ± 0.216 | +0.022, +0.197, +0.116 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, all fluid bins, median | 2.544 | +0.115 ± 0.218 | +0.024, +0.199, +0.123 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.545 | +0.117 ± 0.217 | +0.027, +0.202, +0.120 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.544 | +0.115 ± 0.218 | +0.024, +0.199, +0.123 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.545 | +0.117 ± 0.217 | +0.027, +0.202, +0.120 | no | no |
| parabola fit, bins ×4, mask 1.0 σ, all fluid bins, median | 2.544 | +0.116 ± 0.218 | +0.024, +0.199, +0.123 | no | no |
| parabola fit, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.545 | +0.116 ± 0.216 | +0.027, +0.201, +0.121 | no | no |
| parabola fit, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.544 | +0.116 ± 0.218 | +0.024, +0.199, +0.123 | no | no |
| parabola fit, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.545 | +0.116 ± 0.216 | +0.027, +0.201, +0.121 | no | no |
| smoothed 0.25 σ, bins ×1, course mask, all fluid bins, median | 2.414 | -0.015 ± 0.354 | -0.123, +0.147, -0.069 | no | no |
| smoothed 0.25 σ, bins ×1, course mask, all fluid bins, mean | 2.695 | +0.266 ± 0.084 | +0.272, +0.230, +0.297 | yes | yes |
| smoothed 0.25 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 2.414 | -0.015 ± 0.354 | -0.123, +0.147, -0.069 | no | no |
| smoothed 0.25 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.695 | +0.266 ± 0.084 | +0.272, +0.230, +0.297 | yes | yes |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 2.300 | -0.129 ± 0.139 | -0.179, -0.139, -0.069 | no | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.999 | +0.571 ± 1.948 | +0.147, +0.090, +1.475 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.300 | -0.129 ± 0.139 | -0.179, -0.139, -0.069 | no | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.999 | +0.571 ± 1.948 | +0.147, +0.090, +1.475 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 2.342 | -0.087 ± 0.509 | -0.236, +0.147, -0.171 | no | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.652 | +0.223 ± 0.296 | +0.088, +0.311, +0.272 | no | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.342 | -0.087 ± 0.509 | -0.236, +0.147, -0.171 | no | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.652 | +0.223 ± 0.296 | +0.088, +0.311, +0.272 | no | no |
| smoothed 0.25 σ, bins ×2, course mask, all fluid bins, median | 2.182 | -0.247 ± 0.172 | -0.251, -0.175, -0.314 | yes | yes |
| smoothed 0.25 σ, bins ×2, course mask, all fluid bins, mean | 2.604 | +0.176 ± 0.123 | +0.222, +0.124, +0.181 | no | yes |
| smoothed 0.25 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.182 | -0.247 ± 0.172 | -0.251, -0.175, -0.314 | yes | yes |
| smoothed 0.25 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.604 | +0.176 ± 0.123 | +0.222, +0.124, +0.181 | no | yes |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.159 | -0.270 ± 0.228 | -0.359, -0.175, -0.276 | yes | yes |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.819 | +0.390 ± 1.309 | +0.121, +0.052, +0.997 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.159 | -0.270 ± 0.228 | -0.359, -0.175, -0.276 | yes | yes |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.819 | +0.390 ± 1.309 | +0.121, +0.052, +0.997 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, all fluid bins, median | 2.177 | -0.252 ± 0.335 | -0.373, -0.107, -0.276 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.509 | +0.080 ± 0.387 | -0.099, +0.182, +0.158 | no | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.177 | -0.252 ± 0.335 | -0.373, -0.107, -0.276 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.509 | +0.080 ± 0.387 | -0.099, +0.182, +0.158 | no | no |
| smoothed 0.25 σ, bins ×4, course mask, all fluid bins, median | 2.360 | -0.069 ± 0.160 | -0.138, -0.010, -0.059 | no | no |
| smoothed 0.25 σ, bins ×4, course mask, all fluid bins, mean | 2.363 | -0.065 ± 0.231 | -0.172, +0.000, -0.024 | no | no |
| smoothed 0.25 σ, bins ×4, course mask, less 1.0 σ at each plane, median | 2.360 | -0.069 ± 0.160 | -0.138, -0.010, -0.059 | no | no |
| smoothed 0.25 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.363 | -0.065 ± 0.231 | -0.172, +0.000, -0.024 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 2.356 | -0.073 ± 0.107 | -0.121, -0.038, -0.059 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.393 | -0.036 ± 0.129 | +0.003, -0.095, -0.015 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.356 | -0.073 ± 0.107 | -0.121, -0.038, -0.059 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.393 | -0.036 ± 0.129 | +0.003, -0.095, -0.015 | no | no |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, all fluid bins, median | 2.350 | -0.078 ± 0.202 | -0.163, -0.000, -0.072 | no | no |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.324 | -0.105 ± 0.304 | -0.215, +0.027, -0.127 | no | no |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.350 | -0.078 ± 0.202 | -0.163, -0.000, -0.072 | no | no |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.324 | -0.105 ± 0.304 | -0.215, +0.027, -0.127 | no | no |
| smoothed 0.5 σ, bins ×1, course mask, all fluid bins, mean | 2.512 | +0.083 ± 0.095 | +0.039, +0.100, +0.110 | no | no |
| smoothed 0.5 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 2.429 | +0.000 ± 0.000 | +0.000, +0.000, +0.000 | no | no |
| smoothed 0.5 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.512 | +0.083 ± 0.095 | +0.039, +0.100, +0.110 | no | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 2.412 | -0.017 ± 0.106 | -0.048, -0.034, +0.032 | no | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.536 | +0.107 ± 0.280 | +0.123, -0.012, +0.212 | no | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.412 | -0.017 ± 0.106 | -0.048, -0.034, +0.032 | no | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.536 | +0.107 ± 0.280 | +0.123, -0.012, +0.212 | no | no |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 2.356 | -0.073 ± 0.229 | -0.107, +0.032, -0.142 | no | no |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.456 | +0.027 ± 0.332 | -0.098, +0.168, +0.012 | no | no |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.356 | -0.073 ± 0.229 | -0.107, +0.032, -0.142 | no | no |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.456 | +0.027 ± 0.332 | -0.098, +0.168, +0.012 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, all fluid bins, median | 2.324 | -0.104 ± 0.237 | -0.214, -0.063, -0.037 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, all fluid bins, mean | 2.420 | -0.009 ± 0.170 | -0.086, +0.043, +0.016 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.324 | -0.104 ± 0.237 | -0.214, -0.063, -0.037 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.420 | -0.009 ± 0.170 | -0.086, +0.043, +0.016 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.322 | -0.107 ± 0.233 | -0.214, -0.070, -0.037 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.428 | -0.000 ± 0.193 | -0.067, -0.019, +0.085 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.322 | -0.107 ± 0.233 | -0.214, -0.070, -0.037 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.428 | -0.000 ± 0.193 | -0.067, -0.019, +0.085 | no | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, all fluid bins, median | 2.293 | -0.136 ± 0.315 | -0.280, -0.042, -0.084 | no | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.381 | -0.048 ± 0.324 | -0.172, +0.088, -0.061 | no | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.293 | -0.136 ± 0.315 | -0.280, -0.042, -0.084 | no | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.381 | -0.048 ± 0.324 | -0.172, +0.088, -0.061 | no | no |
| smoothed 0.5 σ, bins ×4, course mask, all fluid bins, median | 2.360 | -0.069 ± 0.160 | -0.138, -0.010, -0.059 | no | no |
| smoothed 0.5 σ, bins ×4, course mask, all fluid bins, mean | 2.363 | -0.065 ± 0.231 | -0.172, +0.000, -0.024 | no | no |
| smoothed 0.5 σ, bins ×4, course mask, less 1.0 σ at each plane, median | 2.360 | -0.069 ± 0.160 | -0.138, -0.010, -0.059 | no | no |
| smoothed 0.5 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.363 | -0.065 ± 0.231 | -0.172, +0.000, -0.024 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 2.356 | -0.073 ± 0.107 | -0.121, -0.038, -0.059 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.393 | -0.036 ± 0.129 | +0.003, -0.095, -0.015 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.356 | -0.073 ± 0.107 | -0.121, -0.038, -0.059 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.393 | -0.036 ± 0.129 | +0.003, -0.095, -0.015 | no | no |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, all fluid bins, median | 2.350 | -0.078 ± 0.202 | -0.163, -0.000, -0.072 | no | no |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.324 | -0.105 ± 0.304 | -0.215, +0.027, -0.127 | no | no |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.350 | -0.078 ± 0.202 | -0.163, -0.000, -0.072 | no | no |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.324 | -0.105 ± 0.304 | -0.215, +0.027, -0.127 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, all fluid bins, median | 2.454 | +0.025 ± 0.175 | -0.036, +0.102, +0.010 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, all fluid bins, mean | 2.455 | +0.027 ± 0.196 | -0.055, +0.102, +0.033 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 2.454 | +0.025 ± 0.175 | -0.036, +0.102, +0.010 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.455 | +0.027 ± 0.196 | -0.055, +0.102, +0.033 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 2.445 | +0.016 ± 0.030 | +0.022, +0.025, +0.003 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.471 | +0.042 ± 0.033 | +0.054, +0.045, +0.028 | no | yes |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.445 | +0.016 ± 0.030 | +0.022, +0.025, +0.003 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.471 | +0.042 ± 0.033 | +0.054, +0.045, +0.028 | no | yes |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 2.504 | +0.075 ± 0.338 | -0.036, +0.227, +0.034 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.481 | +0.053 ± 0.301 | -0.066, +0.177, +0.047 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.504 | +0.075 ± 0.338 | -0.036, +0.227, +0.034 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.481 | +0.053 ± 0.301 | -0.066, +0.177, +0.047 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, all fluid bins, median | 2.439 | +0.010 ± 0.173 | -0.063, +0.076, +0.018 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, all fluid bins, mean | 2.420 | -0.009 ± 0.212 | -0.103, +0.064, +0.012 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.439 | +0.010 ± 0.173 | -0.063, +0.076, +0.018 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.420 | -0.009 ± 0.212 | -0.103, +0.064, +0.012 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.438 | +0.009 ± 0.128 | -0.046, +0.056, +0.018 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.428 | -0.001 ± 0.050 | -0.020, +0.020, -0.002 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.438 | +0.009 ± 0.128 | -0.046, +0.056, +0.018 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.428 | -0.001 ± 0.050 | -0.020, +0.020, -0.002 | no | no |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, all fluid bins, median | 2.452 | +0.023 ± 0.216 | -0.063, +0.111, +0.021 | no | no |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.431 | +0.002 ± 0.292 | -0.111, +0.123, -0.007 | no | no |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.452 | +0.023 ± 0.216 | -0.063, +0.111, +0.021 | no | no |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.431 | +0.002 ± 0.292 | -0.111, +0.123, -0.007 | no | no |
| smoothed 1.0 σ, bins ×4, course mask, all fluid bins, median | 2.383 | -0.045 ± 0.130 | -0.092, +0.012, -0.056 | no | no |
| smoothed 1.0 σ, bins ×4, course mask, all fluid bins, mean | 2.400 | -0.028 ± 0.188 | -0.107, +0.044, -0.022 | no | no |
| smoothed 1.0 σ, bins ×4, course mask, less 1.0 σ at each plane, median | 2.383 | -0.045 ± 0.130 | -0.092, +0.012, -0.056 | no | no |
| smoothed 1.0 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.400 | -0.028 ± 0.188 | -0.107, +0.044, -0.022 | no | no |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 2.395 | -0.034 ± 0.027 | -0.046, -0.025, -0.032 | no | yes |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.417 | -0.011 ± 0.089 | -0.048, -0.009, +0.024 | no | no |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.395 | -0.034 ± 0.027 | -0.046, -0.025, -0.032 | no | yes |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.417 | -0.011 ± 0.089 | -0.048, -0.009, +0.024 | no | no |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, all fluid bins, median | 2.418 | -0.010 ± 0.250 | -0.099, +0.099, -0.030 | no | no |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.420 | -0.009 ± 0.257 | -0.111, +0.096, -0.010 | no | no |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.418 | -0.010 ± 0.250 | -0.099, +0.099, -0.030 | no | no |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.420 | -0.009 ± 0.257 | -0.111, +0.096, -0.010 | no | no |

## Width 10 σ: every choice

Default: s11 2.488, s22 2.438, s33 2.460.

| choice | mean | move ± its paired half-width | paired differences (s11, s22, s33) | beyond the default's half-width | beyond its own half-width |
|---|---|---|---|---|---|
| parabola fit, bins ×1, course mask, all fluid bins, median | 2.460 | -0.002 ± 0.107 | -0.036, +0.046, -0.017 | no | no |
| parabola fit, bins ×1, course mask, all fluid bins, mean | 2.460 | -0.002 ± 0.107 | -0.036, +0.047, -0.017 | no | no |
| parabola fit, bins ×1, course mask, less 1.0 σ at each plane, median | 2.460 | -0.002 ± 0.107 | -0.036, +0.046, -0.017 | no | no |
| parabola fit, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.460 | -0.002 ± 0.107 | -0.036, +0.047, -0.017 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, all fluid bins, median | 2.464 | +0.002 ± 0.108 | -0.031, +0.051, -0.015 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.462 | -0.000 ± 0.107 | -0.034, +0.048, -0.015 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.464 | +0.002 ± 0.108 | -0.031, +0.051, -0.015 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.462 | -0.000 ± 0.107 | -0.034, +0.048, -0.015 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, all fluid bins, median | 2.459 | -0.003 ± 0.107 | -0.037, +0.046, -0.017 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.459 | -0.003 ± 0.107 | -0.037, +0.046, -0.018 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.459 | -0.003 ± 0.107 | -0.037, +0.046, -0.017 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.459 | -0.003 ± 0.107 | -0.037, +0.046, -0.018 | no | no |
| parabola fit, bins ×2, course mask, all fluid bins, median | 2.460 | -0.002 ± 0.116 | -0.041, +0.050, -0.015 | no | no |
| parabola fit, bins ×2, course mask, all fluid bins, mean | 2.461 | -0.001 ± 0.112 | -0.038, +0.049, -0.013 | no | no |
| parabola fit, bins ×2, course mask, less 1.0 σ at each plane, median | 2.460 | -0.002 ± 0.116 | -0.041, +0.050, -0.015 | no | no |
| parabola fit, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.461 | -0.001 ± 0.112 | -0.038, +0.049, -0.013 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, all fluid bins, median | 2.460 | -0.002 ± 0.116 | -0.041, +0.050, -0.015 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.463 | +0.001 ± 0.112 | -0.037, +0.051, -0.011 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.460 | -0.002 ± 0.116 | -0.041, +0.050, -0.015 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.463 | +0.001 ± 0.112 | -0.037, +0.051, -0.011 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, all fluid bins, median | 2.459 | -0.003 ± 0.114 | -0.041, +0.048, -0.015 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.460 | -0.002 ± 0.112 | -0.039, +0.048, -0.014 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.459 | -0.003 ± 0.114 | -0.041, +0.048, -0.015 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.460 | -0.002 ± 0.112 | -0.039, +0.048, -0.014 | no | no |
| parabola fit, bins ×4, course mask, all fluid bins, median | 2.490 | +0.028 ± 0.108 | -0.009, +0.076, +0.017 | no | no |
| parabola fit, bins ×4, course mask, all fluid bins, mean | 2.491 | +0.029 ± 0.108 | -0.008, +0.077, +0.018 | no | no |
| parabola fit, bins ×4, course mask, less 1.0 σ at each plane, median | 2.490 | +0.028 ± 0.108 | -0.009, +0.076, +0.017 | no | no |
| parabola fit, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.491 | +0.029 ± 0.108 | -0.008, +0.077, +0.018 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, all fluid bins, median | 2.490 | +0.028 ± 0.108 | -0.009, +0.076, +0.017 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.491 | +0.029 ± 0.108 | -0.008, +0.077, +0.019 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.490 | +0.028 ± 0.108 | -0.009, +0.076, +0.017 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.491 | +0.029 ± 0.108 | -0.008, +0.077, +0.019 | no | no |
| parabola fit, bins ×4, mask 1.0 σ, all fluid bins, median | 2.490 | +0.028 ± 0.108 | -0.009, +0.076, +0.017 | no | no |
| parabola fit, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.491 | +0.029 ± 0.108 | -0.008, +0.077, +0.018 | no | no |
| parabola fit, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.490 | +0.028 ± 0.108 | -0.009, +0.076, +0.017 | no | no |
| parabola fit, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.491 | +0.029 ± 0.108 | -0.008, +0.077, +0.018 | no | no |
| smoothed 0.25 σ, bins ×1, course mask, all fluid bins, median | 2.546 | +0.084 ± 0.393 | -0.066, +0.249, +0.070 | yes | no |
| smoothed 0.25 σ, bins ×1, course mask, all fluid bins, mean | 2.849 | +0.387 ± 0.428 | +0.277, +0.298, +0.585 | yes | no |
| smoothed 0.25 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 2.546 | +0.084 ± 0.393 | -0.066, +0.249, +0.070 | yes | no |
| smoothed 0.25 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.849 | +0.387 ± 0.428 | +0.277, +0.298, +0.585 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 2.552 | +0.090 ± 0.348 | -0.015, +0.249, +0.037 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.951 | +0.490 ± 0.336 | +0.633, +0.472, +0.363 | yes | yes |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.552 | +0.090 ± 0.348 | -0.015, +0.249, +0.037 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.951 | +0.490 ± 0.336 | +0.633, +0.472, +0.363 | yes | yes |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 2.541 | +0.079 ± 0.223 | +0.019, +0.182, +0.037 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.720 | +0.258 ± 0.231 | +0.364, +0.218, +0.192 | yes | yes |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.541 | +0.079 ± 0.223 | +0.019, +0.182, +0.037 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.720 | +0.258 ± 0.231 | +0.364, +0.218, +0.192 | yes | yes |
| smoothed 0.25 σ, bins ×2, course mask, all fluid bins, median | 2.535 | +0.073 ± 0.298 | +0.029, +0.208, -0.019 | yes | no |
| smoothed 0.25 σ, bins ×2, course mask, all fluid bins, mean | 2.662 | +0.200 ± 0.226 | +0.095, +0.248, +0.257 | yes | no |
| smoothed 0.25 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.535 | +0.073 ± 0.298 | +0.029, +0.208, -0.019 | yes | no |
| smoothed 0.25 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.662 | +0.200 ± 0.226 | +0.095, +0.248, +0.257 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.557 | +0.095 ± 0.342 | +0.134, +0.208, -0.059 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.671 | +0.209 ± 0.175 | +0.157, +0.289, +0.180 | yes | yes |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.557 | +0.095 ± 0.342 | +0.134, +0.208, -0.059 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.671 | +0.209 ± 0.175 | +0.157, +0.289, +0.180 | yes | yes |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, all fluid bins, median | 2.557 | +0.095 ± 0.342 | +0.134, +0.208, -0.059 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.576 | +0.114 ± 0.160 | +0.165, +0.136, +0.041 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.557 | +0.095 ± 0.342 | +0.134, +0.208, -0.059 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.576 | +0.114 ± 0.160 | +0.165, +0.136, +0.041 | yes | no |
| smoothed 0.25 σ, bins ×4, course mask, all fluid bins, median | 2.377 | -0.085 ± 0.068 | -0.098, -0.053, -0.103 | yes | yes |
| smoothed 0.25 σ, bins ×4, course mask, all fluid bins, mean | 2.404 | -0.058 ± 0.074 | -0.074, -0.024, -0.077 | no | no |
| smoothed 0.25 σ, bins ×4, course mask, less 1.0 σ at each plane, median | 2.377 | -0.085 ± 0.068 | -0.098, -0.053, -0.103 | yes | yes |
| smoothed 0.25 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.404 | -0.058 ± 0.074 | -0.074, -0.024, -0.077 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 2.394 | -0.068 ± 0.141 | -0.098, -0.002, -0.103 | yes | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.438 | -0.024 ± 0.157 | -0.081, +0.044, -0.033 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.394 | -0.068 ± 0.141 | -0.098, -0.002, -0.103 | yes | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.438 | -0.024 ± 0.157 | -0.081, +0.044, -0.033 | no | no |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, all fluid bins, median | 2.377 | -0.085 ± 0.068 | -0.098, -0.053, -0.103 | yes | yes |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.404 | -0.058 ± 0.074 | -0.074, -0.024, -0.077 | no | no |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.377 | -0.085 ± 0.068 | -0.098, -0.053, -0.103 | yes | yes |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.404 | -0.058 ± 0.074 | -0.074, -0.024, -0.077 | no | no |
| smoothed 0.5 σ, bins ×1, course mask, all fluid bins, mean | 2.586 | +0.124 ± 0.138 | +0.060, +0.163, +0.149 | yes | no |
| smoothed 0.5 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 2.462 | +0.000 ± 0.000 | +0.000, +0.000, +0.000 | no | no |
| smoothed 0.5 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.586 | +0.124 ± 0.138 | +0.060, +0.163, +0.149 | yes | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 2.475 | +0.013 ± 0.054 | +0.000, +0.038, +0.000 | no | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.616 | +0.154 ± 0.309 | +0.081, +0.297, +0.083 | yes | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.475 | +0.013 ± 0.054 | +0.000, +0.038, +0.000 | no | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.616 | +0.154 ± 0.309 | +0.081, +0.297, +0.083 | yes | no |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 2.450 | -0.012 ± 0.086 | +0.015, +0.000, -0.052 | no | no |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.529 | +0.067 ± 0.114 | +0.079, +0.107, +0.017 | yes | no |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.450 | -0.012 ± 0.086 | +0.015, +0.000, -0.052 | no | no |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.529 | +0.067 ± 0.114 | +0.079, +0.107, +0.017 | yes | no |
| smoothed 0.5 σ, bins ×2, course mask, all fluid bins, median | 2.494 | +0.032 ± 0.150 | -0.006, +0.102, +0.000 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, all fluid bins, mean | 2.487 | +0.025 ± 0.113 | -0.018, +0.073, +0.020 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.494 | +0.032 ± 0.150 | -0.006, +0.102, +0.000 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.487 | +0.025 ± 0.113 | -0.018, +0.073, +0.020 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.485 | +0.023 ± 0.171 | -0.006, +0.102, -0.026 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.480 | +0.018 ± 0.177 | -0.037, +0.099, -0.007 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.485 | +0.023 ± 0.171 | -0.006, +0.102, -0.026 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.480 | +0.018 ± 0.177 | -0.037, +0.099, -0.007 | no | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, all fluid bins, median | 2.459 | -0.003 ± 0.062 | -0.006, +0.024, -0.026 | no | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.446 | -0.016 ± 0.065 | -0.021, +0.013, -0.039 | no | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.459 | -0.003 ± 0.062 | -0.006, +0.024, -0.026 | no | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.446 | -0.016 ± 0.065 | -0.021, +0.013, -0.039 | no | no |
| smoothed 0.5 σ, bins ×4, course mask, all fluid bins, median | 2.377 | -0.085 ± 0.068 | -0.098, -0.053, -0.103 | yes | yes |
| smoothed 0.5 σ, bins ×4, course mask, all fluid bins, mean | 2.404 | -0.058 ± 0.074 | -0.074, -0.024, -0.077 | no | no |
| smoothed 0.5 σ, bins ×4, course mask, less 1.0 σ at each plane, median | 2.377 | -0.085 ± 0.068 | -0.098, -0.053, -0.103 | yes | yes |
| smoothed 0.5 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.404 | -0.058 ± 0.074 | -0.074, -0.024, -0.077 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 2.394 | -0.068 ± 0.141 | -0.098, -0.002, -0.103 | yes | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.438 | -0.024 ± 0.157 | -0.081, +0.044, -0.033 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.394 | -0.068 ± 0.141 | -0.098, -0.002, -0.103 | yes | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.438 | -0.024 ± 0.157 | -0.081, +0.044, -0.033 | no | no |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, all fluid bins, median | 2.377 | -0.085 ± 0.068 | -0.098, -0.053, -0.103 | yes | yes |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.404 | -0.058 ± 0.074 | -0.074, -0.024, -0.077 | no | no |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.377 | -0.085 ± 0.068 | -0.098, -0.053, -0.103 | yes | yes |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.404 | -0.058 ± 0.074 | -0.074, -0.024, -0.077 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, all fluid bins, median | 2.408 | -0.054 ± 0.118 | -0.094, -0.001, -0.067 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, all fluid bins, mean | 2.429 | -0.033 ± 0.093 | -0.050, +0.010, -0.058 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 2.408 | -0.054 ± 0.118 | -0.094, -0.001, -0.067 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.429 | -0.033 ± 0.093 | -0.050, +0.010, -0.058 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 2.400 | -0.062 ± 0.166 | -0.124, +0.009, -0.069 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.432 | -0.030 ± 0.178 | -0.082, +0.052, -0.059 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.400 | -0.062 ± 0.166 | -0.124, +0.009, -0.069 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.432 | -0.030 ± 0.178 | -0.082, +0.052, -0.059 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 2.404 | -0.058 ± 0.105 | -0.094, -0.011, -0.069 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.399 | -0.062 ± 0.081 | -0.075, -0.026, -0.087 | yes | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.404 | -0.058 ± 0.105 | -0.094, -0.011, -0.069 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.399 | -0.062 ± 0.081 | -0.075, -0.026, -0.087 | yes | no |
| smoothed 1.0 σ, bins ×2, course mask, all fluid bins, median | 2.404 | -0.058 ± 0.112 | -0.063, -0.011, -0.100 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, all fluid bins, mean | 2.435 | -0.027 ± 0.100 | -0.051, +0.020, -0.048 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.404 | -0.058 ± 0.112 | -0.063, -0.011, -0.100 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.435 | -0.027 ± 0.100 | -0.051, +0.020, -0.048 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.403 | -0.059 ± 0.135 | -0.078, +0.003, -0.100 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.434 | -0.028 ± 0.161 | -0.077, +0.046, -0.051 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.403 | -0.059 ± 0.135 | -0.078, +0.003, -0.100 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.434 | -0.028 ± 0.161 | -0.077, +0.046, -0.051 | no | no |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, all fluid bins, median | 2.392 | -0.070 ± 0.079 | -0.063, -0.042, -0.105 | yes | no |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.406 | -0.056 ± 0.077 | -0.068, -0.021, -0.079 | no | no |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.392 | -0.070 ± 0.079 | -0.063, -0.042, -0.105 | yes | no |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.406 | -0.056 ± 0.077 | -0.068, -0.021, -0.079 | no | no |
| smoothed 1.0 σ, bins ×4, course mask, all fluid bins, median | 2.435 | -0.027 ± 0.106 | -0.048, +0.023, -0.055 | no | no |
| smoothed 1.0 σ, bins ×4, course mask, all fluid bins, mean | 2.422 | -0.040 ± 0.101 | -0.060, +0.007, -0.066 | no | no |
| smoothed 1.0 σ, bins ×4, course mask, less 1.0 σ at each plane, median | 2.435 | -0.027 ± 0.106 | -0.048, +0.023, -0.055 | no | no |
| smoothed 1.0 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.422 | -0.040 ± 0.101 | -0.060, +0.007, -0.066 | no | no |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 2.439 | -0.023 ± 0.121 | -0.048, +0.033, -0.055 | no | no |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.442 | -0.020 ± 0.141 | -0.067, +0.043, -0.037 | no | no |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.439 | -0.023 ± 0.121 | -0.048, +0.033, -0.055 | no | no |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.442 | -0.020 ± 0.141 | -0.067, +0.043, -0.037 | no | no |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, all fluid bins, median | 2.435 | -0.027 ± 0.106 | -0.048, +0.023, -0.055 | no | no |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.422 | -0.040 ± 0.101 | -0.060, +0.007, -0.066 | no | no |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.435 | -0.027 ± 0.106 | -0.048, +0.023, -0.055 | no | no |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.422 | -0.040 ± 0.101 | -0.060, +0.007, -0.066 | no | no |

## Width 12 σ: every choice

Default: s11 2.358, s22 2.492, s33 2.414.

| choice | mean | move ± its paired half-width | paired differences (s11, s22, s33) | beyond the default's half-width | beyond its own half-width |
|---|---|---|---|---|---|
| parabola fit, bins ×1, course mask, all fluid bins, median | 2.448 | +0.027 ± 0.098 | +0.072, -0.001, +0.009 | no | no |
| parabola fit, bins ×1, course mask, all fluid bins, mean | 2.448 | +0.027 ± 0.097 | +0.072, +0.000, +0.009 | no | no |
| parabola fit, bins ×1, course mask, less 1.0 σ at each plane, median | 2.448 | +0.027 ± 0.098 | +0.072, -0.001, +0.009 | no | no |
| parabola fit, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.448 | +0.027 ± 0.097 | +0.072, +0.000, +0.009 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, all fluid bins, median | 2.448 | +0.027 ± 0.099 | +0.073, -0.001, +0.009 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.448 | +0.027 ± 0.097 | +0.072, +0.000, +0.009 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.448 | +0.027 ± 0.099 | +0.073, -0.001, +0.009 | no | no |
| parabola fit, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.448 | +0.027 ± 0.097 | +0.072, +0.000, +0.009 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, all fluid bins, median | 2.448 | +0.026 ± 0.097 | +0.071, -0.001, +0.008 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.448 | +0.026 ± 0.097 | +0.071, -0.000, +0.008 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.448 | +0.026 ± 0.097 | +0.071, -0.001, +0.008 | no | no |
| parabola fit, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.448 | +0.026 ± 0.097 | +0.071, -0.000, +0.008 | no | no |
| parabola fit, bins ×2, course mask, all fluid bins, median | 2.450 | +0.029 ± 0.094 | +0.073, +0.004, +0.010 | no | no |
| parabola fit, bins ×2, course mask, all fluid bins, mean | 2.449 | +0.028 ± 0.095 | +0.072, +0.002, +0.009 | no | no |
| parabola fit, bins ×2, course mask, less 1.0 σ at each plane, median | 2.450 | +0.029 ± 0.094 | +0.073, +0.004, +0.010 | no | no |
| parabola fit, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.449 | +0.028 ± 0.095 | +0.072, +0.002, +0.009 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, all fluid bins, median | 2.451 | +0.030 ± 0.095 | +0.074, +0.004, +0.011 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.449 | +0.028 ± 0.095 | +0.072, +0.003, +0.009 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.451 | +0.030 ± 0.095 | +0.074, +0.004, +0.011 | no | no |
| parabola fit, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.449 | +0.028 ± 0.095 | +0.072, +0.003, +0.009 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, all fluid bins, median | 2.450 | +0.029 ± 0.094 | +0.073, +0.004, +0.010 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.448 | +0.027 ± 0.095 | +0.071, +0.002, +0.008 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.450 | +0.029 ± 0.094 | +0.073, +0.004, +0.010 | no | no |
| parabola fit, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.448 | +0.027 ± 0.095 | +0.071, +0.002, +0.008 | no | no |
| parabola fit, bins ×4, course mask, all fluid bins, median | 2.467 | +0.045 ± 0.095 | +0.089, +0.018, +0.029 | no | no |
| parabola fit, bins ×4, course mask, all fluid bins, mean | 2.467 | +0.045 ± 0.094 | +0.089, +0.019, +0.028 | no | no |
| parabola fit, bins ×4, course mask, less 1.0 σ at each plane, median | 2.467 | +0.045 ± 0.095 | +0.089, +0.018, +0.029 | no | no |
| parabola fit, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.467 | +0.045 ± 0.094 | +0.089, +0.019, +0.028 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, all fluid bins, median | 2.467 | +0.045 ± 0.095 | +0.089, +0.018, +0.029 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.467 | +0.046 ± 0.094 | +0.089, +0.020, +0.029 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.467 | +0.045 ± 0.095 | +0.089, +0.018, +0.029 | no | no |
| parabola fit, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.467 | +0.046 ± 0.094 | +0.089, +0.020, +0.029 | no | no |
| parabola fit, bins ×4, mask 1.0 σ, all fluid bins, median | 2.467 | +0.045 ± 0.095 | +0.089, +0.018, +0.029 | no | no |
| parabola fit, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.467 | +0.045 ± 0.094 | +0.089, +0.019, +0.028 | no | no |
| parabola fit, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.467 | +0.045 ± 0.095 | +0.089, +0.018, +0.029 | no | no |
| parabola fit, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.467 | +0.045 ± 0.094 | +0.089, +0.019, +0.028 | no | no |
| smoothed 0.25 σ, bins ×1, course mask, all fluid bins, median | 2.466 | +0.044 ± 0.132 | +0.024, +0.004, +0.104 | no | no |
| smoothed 0.25 σ, bins ×1, course mask, all fluid bins, mean | 3.009 | +0.587 ± 1.282 | +1.183, +0.282, +0.297 | yes | no |
| smoothed 0.25 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 2.466 | +0.044 ± 0.132 | +0.024, +0.004, +0.104 | no | no |
| smoothed 0.25 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 3.009 | +0.587 ± 1.282 | +1.183, +0.282, +0.297 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 2.428 | +0.007 ± 0.211 | -0.050, -0.034, +0.104 | no | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.622 | +0.201 ± 0.722 | -0.079, +0.180, +0.501 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.428 | +0.007 ± 0.211 | -0.050, -0.034, +0.104 | no | no |
| smoothed 0.25 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.622 | +0.201 ± 0.722 | -0.079, +0.180, +0.501 | yes | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 2.455 | +0.034 ± 0.183 | +0.024, -0.034, +0.112 | no | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.557 | +0.136 ± 0.489 | +0.060, -0.012, +0.359 | no | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.455 | +0.034 ± 0.183 | +0.024, -0.034, +0.112 | no | no |
| smoothed 0.25 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.557 | +0.136 ± 0.489 | +0.060, -0.012, +0.359 | no | no |
| smoothed 0.25 σ, bins ×2, course mask, all fluid bins, median | 2.443 | +0.022 ± 0.125 | +0.071, +0.024, -0.030 | no | no |
| smoothed 0.25 σ, bins ×2, course mask, all fluid bins, mean | 2.549 | +0.128 ± 0.202 | +0.213, +0.121, +0.051 | no | no |
| smoothed 0.25 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.443 | +0.022 ± 0.125 | +0.071, +0.024, -0.030 | no | no |
| smoothed 0.25 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.549 | +0.128 ± 0.202 | +0.213, +0.121, +0.051 | no | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.432 | +0.010 ± 0.132 | +0.071, -0.010, -0.030 | no | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.612 | +0.190 ± 0.361 | +0.350, +0.066, +0.155 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.432 | +0.010 ± 0.132 | +0.071, -0.010, -0.030 | no | no |
| smoothed 0.25 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.612 | +0.190 ± 0.361 | +0.350, +0.066, +0.155 | yes | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, all fluid bins, median | 2.420 | -0.002 ± 0.078 | +0.012, -0.038, +0.021 | no | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.441 | +0.020 ± 0.166 | +0.043, -0.055, +0.072 | no | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.420 | -0.002 ± 0.078 | +0.012, -0.038, +0.021 | no | no |
| smoothed 0.25 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.441 | +0.020 ± 0.166 | +0.043, -0.055, +0.072 | no | no |
| smoothed 0.25 σ, bins ×4, course mask, all fluid bins, median | 2.389 | -0.032 ± 0.079 | -0.001, -0.065, -0.029 | no | no |
| smoothed 0.25 σ, bins ×4, course mask, all fluid bins, mean | 2.394 | -0.027 ± 0.087 | +0.008, -0.063, -0.027 | no | no |
| smoothed 0.25 σ, bins ×4, course mask, less 1.0 σ at each plane, median | 2.389 | -0.032 ± 0.079 | -0.001, -0.065, -0.029 | no | no |
| smoothed 0.25 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.394 | -0.027 ± 0.087 | +0.008, -0.063, -0.027 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 2.392 | -0.030 ± 0.088 | +0.006, -0.065, -0.029 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.414 | -0.007 ± 0.169 | +0.070, -0.057, -0.034 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.392 | -0.030 ± 0.088 | +0.006, -0.065, -0.029 | no | no |
| smoothed 0.25 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.414 | -0.007 ± 0.169 | +0.070, -0.057, -0.034 | no | no |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, all fluid bins, median | 2.389 | -0.032 ± 0.079 | -0.001, -0.065, -0.029 | no | no |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.394 | -0.027 ± 0.087 | +0.008, -0.063, -0.027 | no | no |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.389 | -0.032 ± 0.079 | -0.001, -0.065, -0.029 | no | no |
| smoothed 0.25 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.394 | -0.027 ± 0.087 | +0.008, -0.063, -0.027 | no | no |
| smoothed 0.5 σ, bins ×1, course mask, all fluid bins, mean | 2.487 | +0.066 ± 0.069 | +0.098, +0.048, +0.051 | no | no |
| smoothed 0.5 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 2.421 | +0.000 ± 0.000 | +0.000, +0.000, +0.000 | no | no |
| smoothed 0.5 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.487 | +0.066 ± 0.069 | +0.098, +0.048, +0.051 | no | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 2.386 | -0.035 ± 0.151 | +0.000, -0.105, +0.000 | no | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.476 | +0.054 ± 0.170 | +0.128, -0.007, +0.042 | no | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.386 | -0.035 ± 0.151 | +0.000, -0.105, +0.000 | no | no |
| smoothed 0.5 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.476 | +0.054 ± 0.170 | +0.128, -0.007, +0.042 | no | no |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 2.391 | -0.031 ± 0.177 | -0.024, -0.105, +0.037 | no | no |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.429 | +0.008 ± 0.094 | +0.025, -0.036, +0.034 | no | no |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.391 | -0.031 ± 0.177 | -0.024, -0.105, +0.037 | no | no |
| smoothed 0.5 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.429 | +0.008 ± 0.094 | +0.025, -0.036, +0.034 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, all fluid bins, median | 2.416 | -0.005 ± 0.100 | +0.041, -0.029, -0.028 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, all fluid bins, mean | 2.448 | +0.027 ± 0.104 | +0.074, -0.005, +0.012 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.416 | -0.005 ± 0.100 | +0.041, -0.029, -0.028 | no | no |
| smoothed 0.5 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.448 | +0.027 ± 0.104 | +0.074, -0.005, +0.012 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.411 | -0.010 ± 0.112 | +0.041, -0.043, -0.028 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.441 | +0.020 ± 0.134 | +0.080, -0.024, +0.003 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.411 | -0.010 ± 0.112 | +0.041, -0.043, -0.028 | no | no |
| smoothed 0.5 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.441 | +0.020 ± 0.134 | +0.080, -0.024, +0.003 | no | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, all fluid bins, median | 2.386 | -0.036 ± 0.090 | -0.004, -0.075, -0.028 | no | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.406 | -0.015 ± 0.094 | +0.013, -0.058, -0.001 | no | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.386 | -0.036 ± 0.090 | -0.004, -0.075, -0.028 | no | no |
| smoothed 0.5 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.406 | -0.015 ± 0.094 | +0.013, -0.058, -0.001 | no | no |
| smoothed 0.5 σ, bins ×4, course mask, all fluid bins, median | 2.389 | -0.032 ± 0.079 | -0.001, -0.065, -0.029 | no | no |
| smoothed 0.5 σ, bins ×4, course mask, all fluid bins, mean | 2.394 | -0.027 ± 0.087 | +0.008, -0.063, -0.027 | no | no |
| smoothed 0.5 σ, bins ×4, course mask, less 1.0 σ at each plane, median | 2.389 | -0.032 ± 0.079 | -0.001, -0.065, -0.029 | no | no |
| smoothed 0.5 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.394 | -0.027 ± 0.087 | +0.008, -0.063, -0.027 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 2.392 | -0.030 ± 0.088 | +0.006, -0.065, -0.029 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.414 | -0.007 ± 0.169 | +0.070, -0.057, -0.034 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.392 | -0.030 ± 0.088 | +0.006, -0.065, -0.029 | no | no |
| smoothed 0.5 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.414 | -0.007 ± 0.169 | +0.070, -0.057, -0.034 | no | no |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, all fluid bins, median | 2.389 | -0.032 ± 0.079 | -0.001, -0.065, -0.029 | no | no |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.394 | -0.027 ± 0.087 | +0.008, -0.063, -0.027 | no | no |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.389 | -0.032 ± 0.079 | -0.001, -0.065, -0.029 | no | no |
| smoothed 0.5 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.394 | -0.027 ± 0.087 | +0.008, -0.063, -0.027 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, all fluid bins, median | 2.451 | +0.029 ± 0.125 | +0.080, -0.021, +0.029 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, all fluid bins, mean | 2.438 | +0.017 ± 0.131 | +0.065, -0.039, +0.025 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, less 1.0 σ at each plane, median | 2.451 | +0.029 ± 0.125 | +0.080, -0.021, +0.029 | no | no |
| smoothed 1.0 σ, bins ×1, course mask, less 1.0 σ at each plane, mean | 2.438 | +0.017 ± 0.131 | +0.065, -0.039, +0.025 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, all fluid bins, median | 2.452 | +0.031 ± 0.135 | +0.088, -0.021, +0.025 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, all fluid bins, mean | 2.452 | +0.031 ± 0.188 | +0.118, -0.020, -0.005 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, median | 2.452 | +0.031 ± 0.135 | +0.088, -0.021, +0.025 | no | no |
| smoothed 1.0 σ, bins ×1, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.452 | +0.031 ± 0.188 | +0.118, -0.020, -0.005 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, all fluid bins, median | 2.447 | +0.026 ± 0.095 | +0.059, -0.016, +0.035 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, all fluid bins, mean | 2.438 | +0.017 ± 0.091 | +0.054, -0.019, +0.017 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, median | 2.447 | +0.026 ± 0.095 | +0.059, -0.016, +0.035 | no | no |
| smoothed 1.0 σ, bins ×1, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.438 | +0.017 ± 0.091 | +0.054, -0.019, +0.017 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, all fluid bins, median | 2.433 | +0.012 ± 0.095 | +0.036, -0.032, +0.031 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, all fluid bins, mean | 2.431 | +0.010 ± 0.131 | +0.060, -0.045, +0.014 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, less 1.0 σ at each plane, median | 2.433 | +0.012 ± 0.095 | +0.036, -0.032, +0.031 | no | no |
| smoothed 1.0 σ, bins ×2, course mask, less 1.0 σ at each plane, mean | 2.431 | +0.010 ± 0.131 | +0.060, -0.045, +0.014 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, all fluid bins, median | 2.432 | +0.010 ± 0.093 | +0.038, -0.032, +0.026 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, all fluid bins, mean | 2.437 | +0.015 ± 0.142 | +0.080, -0.028, -0.006 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, median | 2.432 | +0.010 ± 0.093 | +0.038, -0.032, +0.026 | no | no |
| smoothed 1.0 σ, bins ×2, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.437 | +0.015 ± 0.142 | +0.080, -0.028, -0.006 | no | no |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, all fluid bins, median | 2.431 | +0.009 ± 0.077 | +0.035, -0.025, +0.018 | no | no |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, all fluid bins, mean | 2.424 | +0.003 ± 0.082 | +0.035, -0.031, +0.004 | no | no |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, median | 2.431 | +0.009 ± 0.077 | +0.035, -0.025, +0.018 | no | no |
| smoothed 1.0 σ, bins ×2, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.424 | +0.003 ± 0.082 | +0.035, -0.031, +0.004 | no | no |
| smoothed 1.0 σ, bins ×4, course mask, all fluid bins, median | 2.426 | +0.005 ± 0.088 | +0.034, -0.035, +0.014 | no | no |
| smoothed 1.0 σ, bins ×4, course mask, all fluid bins, mean | 2.426 | +0.004 ± 0.094 | +0.040, -0.035, +0.008 | no | no |
| smoothed 1.0 σ, bins ×4, course mask, less 1.0 σ at each plane, median | 2.426 | +0.005 ± 0.088 | +0.034, -0.035, +0.014 | no | no |
| smoothed 1.0 σ, bins ×4, course mask, less 1.0 σ at each plane, mean | 2.426 | +0.004 ± 0.094 | +0.040, -0.035, +0.008 | no | no |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, all fluid bins, median | 2.426 | +0.004 ± 0.105 | +0.049, -0.035, -0.001 | no | no |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, all fluid bins, mean | 2.439 | +0.018 ± 0.138 | +0.081, -0.026, -0.001 | no | no |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, median | 2.426 | +0.004 ± 0.105 | +0.049, -0.035, -0.001 | no | no |
| smoothed 1.0 σ, bins ×4, mask 0.3 σ, less 1.0 σ at each plane, mean | 2.439 | +0.018 ± 0.138 | +0.081, -0.026, -0.001 | no | no |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, all fluid bins, median | 2.426 | +0.005 ± 0.088 | +0.034, -0.035, +0.014 | no | no |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, all fluid bins, mean | 2.426 | +0.004 ± 0.094 | +0.040, -0.035, +0.008 | no | no |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, median | 2.426 | +0.005 ± 0.088 | +0.034, -0.035, +0.014 | no | no |
| smoothed 1.0 σ, bins ×4, mask 1.0 σ, less 1.0 σ at each plane, mean | 2.426 | +0.004 ± 0.094 | +0.040, -0.035, +0.008 | no | no |
