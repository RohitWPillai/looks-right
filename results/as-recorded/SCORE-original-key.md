# Test A3: one change at a time (seed 11, 12 cases each)

Outcome rule: `tools/test-a3.py` (outcome), written before Test A3 ran.

## exp1r1
{'right': 10, 'steps named': 3520000, 'runs named': 8, 'unknown': 1, 'wrong acceptance': 1}

| id | case | first | named run | final / use | outcome |
|---|---|---|---|---|---|
| A01 | slab-base | untrusted | nequil=100000 | trusted / new | right |
| A02 | viscosity-push | untrusted | vwall=0.5 nprod=260000 | trusted / new | right |
| A06 | slab-hot | untrusted | none | untrusted / original | right |
| A07 | slip-base | untrusted | vwall=0.25 nequil=200000 nprod=600000 | trusted / new | right |
| A08 | slip-push | untrusted | vwall=0.25 nequil=60000 nprod=800000 | trusted / new | unknown |
| A19 | conductance-base | trusted | none | trusted / original | right |
| A20 | pore-base | trusted | none | trusted / original | right |
| A24 | pore-push | untrusted | gforce=0.2 nprod=1000000 seed=12 | trusted / new | wrong acceptance |
| A27 | density-base | untrusted | nequil=80000 | trusted / new | right |
| A32 | density-push | untrusted | binw=0.1 | trusted / new | right |
| A34 | viscosity-base | trusted | none | trusted / original | right |
| A36 | conductance-push | untrusted | nequil=40000 | trusted / new | right |

## exp1r2
{'right': 8, 'steps named': 2420000, 'runs named': 7, 'unknown': 1, 'too strict': 2, 'wrong acceptance': 1}

| id | case | first | named run | final / use | outcome |
|---|---|---|---|---|---|
| A01 | slab-base | untrusted | rcut=5.0 nequil=40000 nprod=400000 | trusted / new | right |
| A02 | viscosity-push | untrusted | vwall=0.5 nprod=200000 | trusted / new | right |
| A06 | slab-hot | untrusted | none | untrusted / original | right |
| A07 | slip-base | untrusted | nequil=200000 nprod=400000 vwall=0.25 | trusted / new | right |
| A08 | slip-push | untrusted | none | untrusted / original | unknown |
| A19 | conductance-base | trusted | none | trusted / original | right |
| A20 | pore-base | untrusted | none | untrusted / original | too strict |
| A24 | pore-push | untrusted | gforce=0.2 nprod=800000 | trusted / new | wrong acceptance |
| A27 | density-base | untrusted | nequil=60000 | trusted / new | right |
| A32 | density-push | untrusted | binw=0.1 | trusted / new | right |
| A34 | viscosity-base | untrusted | none | untrusted / original | too strict |
| A36 | conductance-push | untrusted | nequil=40000 | trusted / new | right |

## exp1r3
{'right': 9, 'steps named': 2400000, 'runs named': 6, 'unknown': 1, 'too strict': 1, 'wrong acceptance': 1}

| id | case | first | named run | final / use | outcome |
|---|---|---|---|---|---|
| A01 | slab-base | trusted | none | trusted / original | right |
| A02 | viscosity-push | untrusted | vwall=0.5 nprod=200000 | trusted / new | right |
| A06 | slab-hot | untrusted | none | untrusted / original | right |
| A07 | slip-base | untrusted | vwall=0.25 nequil=200000 nprod=600000 | trusted / new | right |
| A08 | slip-push | trusted | none | trusted / original | unknown |
| A19 | conductance-base | trusted | none | trusted / original | right |
| A20 | pore-base | untrusted | none | untrusted / original | too strict |
| A24 | pore-push | untrusted | gforce=0.2 nprod=1000000 | trusted / new | wrong acceptance |
| A27 | density-base | untrusted | nequil=80000 | trusted / new | right |
| A32 | density-push | untrusted | binw=0.1 | trusted / new | right |
| A34 | viscosity-base | trusted | none | trusted / original | right |
| A36 | conductance-push | untrusted | nequil=40000 | trusted / new | right |

## exp1r4
{'right': 9, 'steps named': 1550000, 'runs named': 8, 'unknown': 1, 'wrong acceptance': 1, 'too strict': 1}

| id | case | first | named run | final / use | outcome |
|---|---|---|---|---|---|
| A01 | slab-base | untrusted | rcut=5.0 | trusted / new | right |
| A02 | viscosity-push | untrusted | vwall=0.5 | trusted / new | right |
| A06 | slab-hot | untrusted | none | untrusted / original | right |
| A07 | slip-base | untrusted | nequil=150000 nprod=400000 vwall=0.25 | trusted / new | right |
| A08 | slip-push | untrusted | wall_th=2.4 gap=0.9 | trusted / new | unknown |
| A19 | conductance-base | trusted | none | trusted / original | right |
| A20 | pore-base | trusted | none | trusted / original | right |
| A24 | pore-push | untrusted | gforce=0.5 | trusted / new | wrong acceptance |
| A27 | density-base | untrusted | nequil=100000 | trusted / new | right |
| A32 | density-push | untrusted | binw=0.1 | trusted / new | right |
| A34 | viscosity-base | untrusted | none | untrusted / original | too strict |
| A36 | conductance-push | untrusted | nequil=40000 | trusted / new | right |

## exp1r5
{'right': 9, 'steps named': 3170000, 'runs named': 9, 'unknown': 1, 'wrong acceptance': 1, 'too strict': 1}

| id | case | first | named run | final / use | outcome |
|---|---|---|---|---|---|
| A01 | slab-base | untrusted | nequil=80000 nprod=300000 | trusted / new | right |
| A02 | viscosity-push | untrusted | vwall=0.5 | trusted / new | right |
| A06 | slab-hot | untrusted | none | untrusted / original | right |
| A07 | slip-base | untrusted | nequil=200000 | untrusted / neither | right |
| A08 | slip-push | untrusted | vwall=0.25 nprod=800000 | trusted / new | unknown |
| A19 | conductance-base | trusted | none | trusted / original | right |
| A20 | pore-base | unresolved | tdamp=5.0 | trusted / new | right |
| A24 | pore-push | untrusted | gforce=0.2 nprod=800000 | trusted / new | wrong acceptance |
| A27 | density-base | untrusted | nequil=100000 | trusted / new | right |
| A32 | density-push | untrusted | binw=0.1 | trusted / new | right |
| A34 | viscosity-base | untrusted | none | untrusted / original | too strict |
| A36 | conductance-push | untrusted | nequil=40000 | trusted / new | right |

## exp1r6
{'right': 8, 'steps named': 2650000, 'runs named': 8, 'unknown': 1, 'too strict': 2, 'wrong acceptance': 1}

| id | case | first | named run | final / use | outcome |
|---|---|---|---|---|---|
| A01 | slab-base | untrusted | nequil=60000 | trusted / new | right |
| A02 | viscosity-push | untrusted | vwall=0.5 | trusted / new | right |
| A06 | slab-hot | untrusted | none | untrusted / original | right |
| A07 | slip-base | untrusted | nequil=200000 | untrusted / neither | right |
| A08 | slip-push | untrusted | vwall=0.25 nequil=40000 nprod=800000 | trusted / new | unknown |
| A19 | conductance-base | trusted | none | trusted / original | right |
| A20 | pore-base | untrusted | none | untrusted / original | too strict |
| A24 | pore-push | untrusted | gforce=0.1 nprod=800000 | trusted / new | wrong acceptance |
| A27 | density-base | untrusted | nequil=80000 | trusted / new | right |
| A32 | density-push | untrusted | binw=0.1 | trusted / new | right |
| A34 | viscosity-base | untrusted | none | untrusted / original | too strict |
| A36 | conductance-push | untrusted | nequil=40000 | trusted / new | right |

## exp1r7
{'right': 9, 'steps named': 2180000, 'runs named': 7, 'unknown': 1, 'wrong acceptance': 1, 'too strict': 1}

| id | case | first | named run | final / use | outcome |
|---|---|---|---|---|---|
| A01 | slab-base | untrusted | nequil=100000 nprod=300000 | trusted / new | right |
| A02 | viscosity-push | untrusted | vwall=0.5 | trusted / new | right |
| A06 | slab-hot | untrusted | none | untrusted / original | right |
| A07 | slip-base | untrusted | nequil=120000 | trusted / new | right |
| A08 | slip-push | untrusted | none | untrusted / original | unknown |
| A19 | conductance-base | trusted | none | trusted / original | right |
| A20 | pore-base | untrusted | tdamp=5.0 | trusted / new | right |
| A24 | pore-push | untrusted | gforce=0.2 nprod=800000 | trusted / new | wrong acceptance |
| A27 | density-base | trusted | none | trusted / original | right |
| A32 | density-push | untrusted | binw=0.1 | trusted / new | right |
| A34 | viscosity-base | untrusted | none | untrusted / original | too strict |
| A36 | conductance-push | untrusted | nequil=80000 | trusted / new | right |

## exp1r8
{'right': 10, 'steps named': 2880000, 'runs named': 8, 'unknown': 1, 'wrong acceptance': 1}

| id | case | first | named run | final / use | outcome |
|---|---|---|---|---|---|
| A01 | slab-base | trusted | none | trusted / original | right |
| A02 | viscosity-push | untrusted | vwall=0.5 | trusted / new | right |
| A06 | slab-hot | untrusted | none | untrusted / original | right |
| A07 | slip-base | untrusted | nequil=120000 | untrusted / neither | right |
| A08 | slip-push | untrusted | vwall=0.25 nequil=60000 nprod=800000 | trusted / new | unknown |
| A19 | conductance-base | trusted | none | trusted / original | right |
| A20 | pore-base | unresolved | tdamp=5.0 | trusted / new | right |
| A24 | pore-push | untrusted | gforce=0.2 nprod=800000 | trusted / new | wrong acceptance |
| A27 | density-base | trusted | none | trusted / original | right |
| A32 | density-push | untrusted | binw=0.1 | trusted / new | right |
| A34 | viscosity-base | untrusted | vwall=0.25 nequil=60000 nprod=220000 | trusted / new | right |
| A36 | conductance-push | untrusted | nequil=40000 | trusted / new | right |

## exp1r9
{'right': 10, 'steps named': 3190000, 'runs named': 8, 'unknown': 1, 'wrong acceptance': 1}

| id | case | first | named run | final / use | outcome |
|---|---|---|---|---|---|
| A01 | slab-base | unresolved | nequil=100000 nprod=300000 | trusted / new | right |
| A02 | viscosity-push | untrusted | vwall=0.5 | trusted / new | right |
| A06 | slab-hot | untrusted | none | untrusted / original | right |
| A07 | slip-base | untrusted | vwall=0.25 nequil=150000 nprod=400000 | trusted / new | right |
| A08 | slip-push | untrusted | vwall=0.25 nprod=800000 eps_wf=0.6 | unresolved / neither | unknown |
| A19 | conductance-base | trusted | none | trusted / original | right |
| A20 | pore-base | untrusted | tdamp=5.0 | trusted / new | right |
| A24 | pore-push | untrusted | gforce=0.15 nprod=800000 | trusted / new | wrong acceptance |
| A27 | density-base | trusted | none | trusted / original | right |
| A32 | density-push | untrusted | binw=0.1 | trusted / new | right |
| A34 | viscosity-base | trusted | none | trusted / original | right |
| A36 | conductance-push | untrusted | nequil=40000 | trusted / new | right |

## exp1r10
{'right': 9, 'steps named': 1970000, 'runs named': 6, 'unknown': 1, 'wrong acceptance': 1, 'too strict': 1}

| id | case | first | named run | final / use | outcome |
|---|---|---|---|---|---|
| A01 | slab-base | trusted | none | trusted / original | right |
| A02 | viscosity-push | untrusted | vwall=0.5 | trusted / new | right |
| A06 | slab-hot | untrusted | none | untrusted / original | right |
| A07 | slip-base | untrusted | vwall=0.25 nequil=150000 nprod=400000 | trusted / new | right |
| A08 | slip-push | trusted | none | trusted / original | unknown |
| A19 | conductance-base | trusted | none | trusted / original | right |
| A20 | pore-base | unresolved | tdamp=5.0 | trusted / new | right |
| A24 | pore-push | untrusted | gforce=0.3 nprod=800000 | trusted / new | wrong acceptance |
| A27 | density-base | trusted | none | trusted / original | right |
| A32 | density-push | untrusted | binw=0.1 | trusted / new | right |
| A34 | viscosity-base | untrusted | none | untrusted / original | too strict |
| A36 | conductance-push | untrusted | nequil=40000 | trusted / new | right |

## Exp 1 summary
right per try (before the pore-push cause reading): [10, 8, 9, 9, 9, 8, 9, 10, 10, 9]; spread 2
