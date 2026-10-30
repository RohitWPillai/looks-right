# Reproducing Looks Right: Polywater

This file is for a scientist who wants to check or rerun the work. Read `README.md` first; it
defines the Auditor, the runs, the looks, the attempts, the experiment (Exp 1, ten attempts) and the answer key. Run every
command from the repository root (https://github.com/RohitWPillai/looks-right).

What is where: `cases/` holds the 12 runs (inputs, logs, the course's analysis scripts and their output, profiles,
plots); `auditor/` the Auditor's instructions, identical to those used, with SHA-256 fingerprints; `key/` the
key, its dated history, the neutral run ids and the narrow-pore case note; `results/` the score tables, every attempt's
answers, call usage and cost, the named runs' analysis output and the four slides explained; `key-checks/` the
plain-code checks of the key (the viscosity stress, the pore thermostat, the pore-width scan); `tools/` and `tests/`
the driver, the scorer, the table tools, the run scripts, `check.py` and their tests; `figures/` the four slides
(`slides/`), the course's plot for each run (`cases/`) and one figure from the earlier test, kept as the key's
evidence (`test-a2/`).

There are three levels, from free to paid.

| level | what it does | what it costs |
|---|---|---|
| 1 | regenerate every score table from the shipped answers and check it against `results/` | nothing: no model calls, no LAMMPS; seconds |
| 2 | rerun one of the 12 runs with LAMMPS, the molecular dynamics program the course uses | CPU only: 10 to 52 s of wall time per run on 8 MPI ranks (8 processes working on one run) |
| 3 | run one new Auditor attempt on all 12 runs | **paid model calls** (table at the end), plus the LAMMPS runs the Auditor names |

## Software and versions used

| what | version as used | where it is recorded |
|---|---|---|
| LAMMPS | 22 Jul 2025, Update 5; MPI build `lmp_mpi`, 8 ranks, 1 OpenMP thread | the header of every `log.lammps` in `cases/` |
| LAMMPS features used | `units lj`, `atom_style atomic`, `lattice fcc`, `pair_style lj/cut`; fixes `nve`, `nve/limit`, `nvt`, `langevin`, `setforce`, `addforce`, `wall/reflect`, `ave/chunk`, `ave/time`; computes `chunk/atom`, `temp`, `temp/com`, `temp/profile`, `ke/atom`, `stress/atom`, `reduce` | the inputs in `cases/` |
| machine for all LAMMPS runs | Apple Mac mini (M4), macOS; LAMMPS and MPI from a conda environment | the experiment record (not released) |
| Python for the course's analysis scripts | Python 3.12 with numpy and matplotlib (and scikit-learn) from conda-forge, versions not pinned at the time | the experiment record |
| Python for `tools/` and `key-checks/` | tested on Python 3.13.12, numpy 2.4.2, matplotlib 3.10.8 | this release |
| Auditor program | Claude Code (the `claude` command line program), run headless (`--print`), with the read-only tools Read, Glob and Grep only, no user or project settings (`--safe-mode`), and a spending cap of `--max-budget-usd 5` per call; full flags in `tools/test-a2.py`, function `agent()` | `tools/test-a2.py` |
| Claude Code version | 2.1.289 for attempts 6 to 10; not recorded for attempts 1 to 5 (8 October; no stream was kept) | the first line of each reduced stream, `results/test-a3/<try>/agents/<id>/audit*.stream.jsonl` (kept from attempt 6 on) |
| Auditor model | `claude-opus-5-5`, default effort, no other settings | `models` in each `audit*.json`; the reduced streams |

Agent programs and models change, so a rerun with today's versions is a new experiment, not a replication. For this reason
every answer used in the scores (all ten attempts of Exp 1) is shipped.

## Level 1: regenerate every results table (free)

```
python3 -m pip install numpy matplotlib pytest     # if needed
python3 tools/check.py
```

`check.py` runs the following into a temporary folder:

```
python3 tools/test-a3.py score --out DIR              # SCORE.md: every try, corrected viscosity key
python3 tools/test-a3.py score original --out DIR     # SCORE-original-key.md: the key before 9 Oct
python3 tools/tables.py --scores DIR --out DIR        # SUMMARY.md, right-per-try.csv, right-per-case.csv (11 runs, and without pore-push)
python3 tools/token-usage.py exp1r1 ... exp1r10 [--cases]       # tokens.md, tokens-by-case.md
python3 tools/call-measures.py exp1r6 ... exp1r10 --by-case     # files-opened.md
python3 key-checks/viscosity-kinetic/summarise.py     # the kinetic-stress table
python3 key-checks/pore-scan/scan-b.py --out DIR      # the pore-width scan
```

It then checks each output against `results/` and, for the two score files, against the files the experiment wrote
at the time (`results/as-recorded/`), whose text matches the regenerated ones line for line. It prints one line per
table and exits 0 only if all match. `python3 tools/check.py --write` rewrites `results/` from the regenerated files.

The `score` commands apply the outcome rule: the code that turns an Auditor's final answer into right, wrong
acceptance, too strict, missed fix, no answer or unknown (`key/KEY.md` defines the words; `tools/test-a3.py`,
function `outcome`).

## Level 2: rerun one run with LAMMPS

Needs an MPI build of LAMMPS with the features listed above (`lmp_mpi` on the PATH, or set `LMP`), and Python with
numpy and matplotlib for the course's analysis script.

```
bash tools/run-case.sh pore-push /tmp/pore-push-rerun seed=11
NP=4 LMP=lmp bash tools/run-case.sh slab-hot /tmp/slab-hot-rerun seed=11
```

The run's fixed settings (for example `-var width 4` for `pore-push`) are applied for you. Extra `NAME=VALUE` pairs
must be `index` variables of the input, the same rule that applies to an Auditor's named run. A relative output path
is taken from the folder you run the command in. The output folder gets the run's whole folder in the course's
layout, as in `cases/<run>/`: for the channel and pore runs, `shared_setup.lmp` and `lammps_io.py` at the top and the
input, `log.lammps`, `lammps.out`, `analysis.out`, profiles and plots in the subfolder. It can then be rerun or
reanalysed in place. The numbers will not match `cases/` exactly on a different machine, MPI rank count or
LAMMPS build; they should agree within run-to-run scatter. The key's evidence runs at seeds 22 and 33
(`results/test-a2/replica-analysis/`) are rerun the same way with `seed=22` or `seed=33`.

## Level 3: run one new Auditor attempt on all 12 runs (paid)

Needs the `claude` program logged in to an account that can use the model, plus everything for level 2. A new attempt
goes in its own results folder, `TESTBED_RESULTS`, so the released `results/` and `tools/check.py` stay exactly as
shipped. The shell wrappers (`run-try.sh`, `run-named-runs.sh`) default it to `new-results/` (ignored by git) and
stop with an error if pointed at `results/`; the Python tools default to the released `results/` when it is not set
(`tools/test-a2.py`, `T1`), so when you run the individual commands below, export it first.

```
bash tools/run-try.sh exp1r11 auditor/exp1-frozen            # writes new-results/
TESTBED_RESULTS=my-results bash tools/run-try.sh exp1r12      # a second new try, into another folder
```

This copies the frozen instructions into `new-results/test-a3/exp1r11/` and fingerprints them, makes a blinded copy of
each run (teaching hints removed, `tools/test-a2.py make_copy`), asks the Auditor's first look on all 12 runs (three
calls at a time), checks the runs it names, runs them with LAMMPS (`tools/run-named-runs.sh`), asks the second look
where a run was named, and scores the attempt into `new-results/SCORE.md`. The attempt's model follows its name's prefix
(the prefix table `MODELS` in `tools/test-a3.py`; a name matching no prefix runs Opus). The individual steps, after
`export TESTBED_RESULTS=new-results` and the folder, copies and fingerprints that `run-try.sh` makes:

```
python3 tools/test-a3.py audit1 <try>                     # first looks (model calls)
python3 tools/test-a3.py runs <try>                       # check the named runs; list them in $TESTBED_RESULTS/reruns.txt
bash tools/run-named-runs.sh                              # run them with LAMMPS into $TESTBED_RESULTS/reruns/<try>-<id>-run/
python3 tools/test-a3.py audit2 <try>                     # second looks (model calls)
python3 tools/test-a3.py score --tries <try>... --out $TESTBED_RESULTS   # score the new tries only
```

The released experiment and its attempts are listed in `tools/experiments.py`, which every tool reads; new attempts are not
added to it.

**Before comparing a new attempt with the published totals.** The automatic score credits any answer on the narrow-pore
Push run that does not trust it, whatever its reason, and prints each such answer's cause. The published totals count
only answers whose cause is the layering, read by hand and recorded in `key/pore-push-cause-reading.csv` (header
only: no Exp 1 answer reached that reading, since every attempt trusted the run). Read the printed causes, record yours
in a file of the same form, and subtract the wrong-reason answers before comparing.

### Cost of an attempt

List price as the Claude Code program reported it for each call (`total_cost_usd`), summed
over an attempt's first and second looks (`results/tokens.md`). Output tokens here count the model's thinking as well as its
written reply (`results/tokens.md` gives the two separately).

| experiment | attempts | list cost, all attempts | per attempt | output tokens per first look |
|---|---|---|---|---|
| Exp 1, Opus | 10 | $42.54 | $3.80 to $4.71, about $4.25 | 4.28 k |

Levels 1 and 2 cost no model calls. In Exp 1 an attempt asked for 6 to 9 named runs at its first looks, all of which
passed the plain-code check and ran (`results/SCORE.md`, "runs named"; `results/test-a3/<try>/runs-checked.txt`),
each at most four times its run's steps. A new attempt may fall outside that range.

## Paths and environment

All tools find the repository from their own location. Overrides: `TESTBED_RESULTS` (the results folder for new
attempts; the shell wrappers default to `new-results/`, the Python tools to the released `results/`), `TESTBED_COPIES`
(where the blinded copies are made; default `/tmp/testbed-copies`), `TESTBED_RUNS` (a folder of `rep-<run>-s<seed>/`
runs to audit instead of `cases/`), `NP`, `LMP`, `MPIRUN`, `PYTHON` for the LAMMPS scripts.

## Changes from the scripts used in the experiment

The scripts in `tools/` are the ones the experiment ran, with these changes only:

- paths made relative to this repository (the map from neutral ids to runs, sealed during the experiment, is
  `key/ids.txt`);
- the frozen-file check reads `auditor/SHA256SUMS` and `results/test-a3/FROZEN.sha256`;
- `score` commands take `--out`, and `--tries` for new attempts in a separate results folder;
- one shared experiment list (`tools/experiments.py`);
- the LAMMPS runs happen on the local machine (`run-case.sh`, `run-named-runs.sh`) instead of over ssh on a Mac mini;
- `call-measures.py` classifies a search path as a file by its name, since the run copies it once checked on
  disk have been deleted.

During Exp 1, after attempts 1 to 5 had run, the agent call began keeping the stream of
tool calls (`--output-format stream-json`, which is why `audit*.stream.jsonl` exists from attempt 6 on), and
`named_changes` was extended to read a named run written as `NAME=OLD→NEW`. They affect logging and malformed requests
only. Attempts 1 to 5 ran without them.

The scoring logic (`outcome`, `fixed`, `score_one`, `verdict`) is unchanged, and the agent call is as it stood from
attempt 6. Shipped call records are reduced: each `audit*.json` keeps only the usage, cost, turn and duration fields, and
each `audit*.stream.jsonl` keeps only the tool calls, with paths made relative to the run copy.
