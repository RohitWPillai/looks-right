# The Auditor's instructions

The Auditor is the AI agent given one finished run and asked whether its result can be trusted for its stated purpose
(`README.md`). `exp1-frozen/` holds the texts exactly as the Auditor received them in Exp 1.
`SHA256SUMS` fingerprints every file, and `tools/test-a2.py` and `tools/test-a3.py` stop with an error before any model call if a file has
changed. Each attempt's own copy is in `results/test-a3/<try>/`, fingerprinted in `results/test-a3/FROZEN.sha256`; every
one of those copies matches the fingerprint the experiment recorded before its first call.

The folder holds three texts: `brief-auditor.md`, the instructions for the Auditor's first look at a run;
`brief-auditor-followup.md`, the instructions for its second look, after plain code has run the one extra simulation
it named (the named run); and `purposes.md`, one line per run saying what the run is for, which is appended to the
instructions. The first-look text includes a materiality rule: before naming a run, estimate how much it would change
the reported number against that number's run-to-run scatter, and name none if the change would be smaller. How the
texts are assembled into one prompt: `tools/test-a2.py` (`audit1`, `audit2`, `purpose_block`).

## What the Auditor sees and can do

The Auditor's working folder is a blinded copy of one run (`tools/test-a2.py`, `make_copy`): the input, `log.lammps`
and shared setup with the course's teaching hints removed (every comment containing "push", "until it breaks",
"narrow", "knob" or "break" is dropped), the command line the run was started with (`command.txt`), the analysis
output, the figures, profiles and data files. The run is labelled by a neutral id such as A24, never by its name
(`key/ids.txt`). The Auditor has the read-only tools Read, Glob and Grep only: it cannot run anything or write a file.
It answers in four fixed lines: verdict (trusted, untrusted or unresolved), run (the named run as `NAME=VALUE` pairs,
or none), cause (one sentence) and evidence (the files and numbers it relied on).

A named run is checked by plain code before it is run: only `index` variables of the input may be changed, at most
four times the original run's steps are allowed, and the run is run once. The Auditor is told not to change a setting
the purpose states; that rule is not enforced by the code but through the score (`key/KEY.md`, the `slab-hot` row).
