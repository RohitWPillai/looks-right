verdict: untrusted
run: nequil=40000
cause: The run was launched with `-var nequil 10000` instead of the 40000 the input says still walls need, so production began before steady state; the hot and cold walls' heat flows had not yet matched, and the two G values are transient numbers rather than steady-state conductances.
evidence: command.txt shows the nequil=10000 override and conductance.in:29 sets the default to 40000; analysis.out gives an in/out imbalance of 53.3% (16.57 vs 7.74), linear-fit R² of 0.986/0.889 and G_bot=0.302 vs G_top=0.536 (1.8x apart); in day1_heat.dat, f_bbot falls about 1470 in the first 10k steps but only about 700 in the last 10k, while f_btop stays near 0 until about 12k and then climbs to 1465, so both slopes are still converging toward each other.
