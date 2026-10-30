| try | calls with a stream | without | reads per call | searches per call | distinct files per call | opened log | opened analysis | opened figure | opened input | opened command | opened data |
|---|---|---|---|---|---|---|---|---|---|---|---|
| exp1r6 | 20 | 0 | 7.0 | 2.4 | 7.9 | 100% | 100% | 45% | 100% | 100% | 80% |
| exp1r7 | 19 | 0 | 7.2 | 2.2 | 7.5 | 100% | 100% | 42% | 100% | 100% | 79% |
| exp1r8 | 20 | 0 | 7.2 | 2.2 | 7.7 | 100% | 100% | 35% | 100% | 100% | 80% |
| exp1r9 | 20 | 0 | 7.2 | 2.2 | 7.6 | 95% | 100% | 45% | 100% | 100% | 70% |
| exp1r10 | 18 | 0 | 6.9 | 2.3 | 7.6 | 100% | 100% | 28% | 100% | 100% | 83% |

By case, over these tries (both looks):
| case | calls | reads per call | distinct files per call | opened log | opened a figure |
|---|---|---|---|---|---|
| A01 slab-base | 8 | 7.0 | 8.1 | 8/8 | 8/8 |
| A02 viscosity-push | 10 | 6.9 | 7.6 | 10/10 | 2/10 |
| A06 slab-hot | 5 | 4.0 | 5.0 | 5/5 | 0/5 |
| A07 slip-base | 10 | 9.3 | 9.4 | 10/10 | 4/10 |
| A08 slip-push | 8 | 9.0 | 9.1 | 8/8 | 1/8 |
| A19 conductance-base | 5 | 7.0 | 8.0 | 5/5 | 0/5 |
| A20 pore-base | 9 | 7.6 | 7.8 | 9/9 | 6/9 |
| A24 pore-push | 10 | 7.8 | 7.7 | 10/10 | 10/10 |
| A27 density-base | 6 | 6.2 | 6.7 | 6/6 | 3/6 |
| A32 density-push | 10 | 4.7 | 5.7 | 10/10 | 0/10 |
| A34 viscosity-base | 6 | 9.3 | 9.7 | 6/6 | 3/6 |
| A36 conductance-push | 10 | 5.8 | 6.8 | 9/10 | 1/10 |

Verdicts per case, one letter per try (exp1r6, exp1r7, exp1r8, exp1r9, exp1r10); T trusted, U untrusted, R unresolved, - no second look:
| case | first look | second look | final |
|---|---|---|---|
| A01 slab-base | U U T R T | T T - T - | T T T T T |
| A02 viscosity-push | U U U U U | T T T T T | T T T T T |
| A06 slab-hot | U U U U U | - - - - - | U U U U U |
| A07 slip-base | U U U U U | U T U T T | U T U T T |
| A08 slip-push | U U U U T | T - T R - | T U T R T |
| A19 conductance-base | T T T T T | - - - - - | T T T T T |
| A20 pore-base | U U R U R | - T T T T | U T T T T |
| A24 pore-push | U U U U U | T T T T T | T T T T T |
| A27 density-base | U T T T T | T - - - - | T T T T T |
| A32 density-push | U U U U U | T T T T T | T T T T T |
| A34 viscosity-base | U U U T U | - - T - - | U U T T U |
| A36 conductance-push | U U U U U | T T T T T | T T T T T |
