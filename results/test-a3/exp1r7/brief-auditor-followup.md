# Auditor follow-up brief
What it is: the brief for the Auditor's second look, after plain code has run the run it named.
Who uses it: the test-bed script, with the first answer appended, to a Claude agent with blank memory, in a folder that
holds the original run (original/) and the new run (new/).
What it refuses: writing files or running anything. No further run is possible.

You audit a molecular dynamics run (LAMMPS, reduced Lennard-Jones units) for a researcher. The run's purpose is given
below; the settings it states are deliberate. An earlier audit of the original run (folder original/) asked for one
more run, which plain code has now done (folder new/: its input, command.txt, log.lammps, analysis output and figures).
The earlier audit is below. Read what you need.

Give the final answer for the purpose: which measurement, if any, can the researcher trust? A difference smaller
than the number's run-to-run scatter, or one that does not change whether the measurement serves the purpose, is not a
reason to distrust it.

Reply with exactly four lines and nothing else:
verdict: <trusted, untrusted or unresolved>
use: <original, new or neither>
cause: <one sentence: why>
evidence: <the files and numbers you based it on>
