| try | first looks | missing | output per first look | of which thinking | second looks | missing | output per second look | turns per call | fresh input | cache reads | output | list cost | call minutes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| exp1r1 | 12 | 0 | 3.77 k | 2.71 k | 8 | 0 | 2.30 k | 9.8 | 0.31 M | 0.80 M | 63.6 k | $3.88 | 14 |
| exp1r2 | 12 | 0 | 3.81 k | 2.61 k | 7 | 0 | 2.57 k | 10.1 | 0.31 M | 0.92 M | 63.7 k | $3.92 | 12 |
| exp1r3 | 12 | 0 | 4.33 k | 3.26 k | 6 | 0 | 2.44 k | 9.7 | 0.29 M | 0.75 M | 66.6 k | $3.80 | 13 |
| exp1r4 | 12 | 0 | 3.96 k | 2.86 k | 8 | 0 | 3.26 k | 9.8 | 0.35 M | 0.92 M | 73.6 k | $4.48 | 14 |
| exp1r5 | 12 | 0 | 4.59 k | 3.49 k | 9 | 0 | 3.11 k | 10.1 | 0.36 M | 1.03 M | 83.1 k | $4.71 | 17 |
| exp1r6 | 12 | 0 | 4.69 k | 3.62 k | 8 | 0 | 2.79 k | 10.3 | 0.34 M | 0.83 M | 78.6 k | $4.46 | 15 |
| exp1r7 | 12 | 0 | 4.38 k | 3.25 k | 7 | 0 | 2.61 k | 10.3 | 0.31 M | 0.90 M | 70.8 k | $4.11 | 14 |
| exp1r8 | 12 | 0 | 4.11 k | 3.04 k | 8 | 0 | 2.98 k | 10.4 | 0.36 M | 0.96 M | 73.2 k | $4.55 | 15 |
| exp1r9 | 12 | 0 | 4.62 k | 3.48 k | 8 | 0 | 3.17 k | 10.4 | 0.36 M | 1.01 M | 80.8 k | $4.71 | 16 |
| exp1r10 | 12 | 0 | 4.50 k | 3.41 k | 6 | 0 | 2.60 k | 10.3 | 0.30 M | 0.84 M | 69.6 k | $3.93 | 13 |
| **exp1, 10 tries** | 120 | 0 | 4.28 k | 3.17 k | 75 | 0 | 2.81 k | 10.1 | 3.29 M | 8.95 M | 723.6 k | $42.54 | 143 |

Mean output tokens (k) per call, by case and look, over exp1r1, exp1r2, exp1r3, exp1r4, exp1r5, exp1r6, exp1r7, exp1r8, exp1r9, exp1r10:
| case | first look | second look |
|---|---|---|
| A01 slab-base | 7.2 (n=10) | 2.8 (n=7) |
| A02 viscosity-push | 1.4 (n=10) | 3.9 (n=10) |
| A06 slab-hot | 1.0 (n=10) | - |
| A07 slip-base | 5.7 (n=10) | 5.0 (n=10) |
| A08 slip-push | 7.2 (n=10) | 5.2 (n=6) |
| A19 conductance-base | 5.0 (n=10) | - |
| A20 pore-base | 5.9 (n=10) | 1.7 (n=5) |
| A24 pore-push | 2.7 (n=10) | 2.0 (n=10) |
| A27 density-base | 2.8 (n=10) | 1.8 (n=6) |
| A32 density-push | 1.0 (n=10) | 1.4 (n=10) |
| A34 viscosity-base | 10.1 (n=10) | 5.4 (n=1) |
| A36 conductance-push | 1.2 (n=10) | 1.3 (n=10) |
