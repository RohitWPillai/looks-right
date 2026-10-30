The new run fixes the problem the earlier audit found. I'm treating its viscosity as the trustworthy one.

verdict: trusted
use: new
cause: At the input's default wall speed of 0.5 the fluid stays at about T*≈1.1 with almost no hot hump in the centre, and the shear profile is linear with little wall slip, so eta≈1.12 measures a nearly isothermal liquid close to T*=1.0. The original run's eta≈0.98 belongs to a liquid at about 2–3.8 and should not be used.
evidence: new/command.txt (-var vwall 0.5 -var nprod 200000); new/analysis.out (dvx/dz=0.0539 with R²=1.000, pxz=-0.0606, eta≈1.123, T(z) 1.08 and 1.11 at the walls and 1.13 at the centre); new/log.lammps (thermo Temp levels off at about 0.96–0.97 from production step 20000 to 200000); new/day1_vx.profile (vx is linear across the bulk, about 107 atoms per bin, bulk density ≈0.72, wall speed ±0.47 against the imposed ±0.5); original/analysis.out (eta≈0.978 at T(z) 2.15–3.18).
