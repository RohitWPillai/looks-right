verdict: untrusted
run: vwall=0.5
cause: The run used wall speed vwall=3.0 (the input's default is 0.5), and viscous heating took the fluid to a peculiar temperature of about 2.2 at the walls and 3.2 at the centre, so the eta of 0.978 is not the T* = 1.0 viscosity; vwall=0.5 cuts the heating about 36-fold and should give an eta near 2, about double the reported value and far beyond the run-to-run scatter.
evidence: command.txt (-var vwall 3.0); analysis.out (dvx/dz=0.3532, pxz=-0.3455, eta≈0.978, T(z) walls ~2.19/2.15, centre ~3.18); day1_KEz.profile (centre <ke>≈4.78 at vx≈0, so T≈3.2); viscosity.in line 31 (vwall default 0.5, "gentle = linear regime").
