# History of the answer key

The answer key (the key) is the author's list of the right final answer for each scored run (`KEY.md`); the Auditor, the AI
agent that judges each run, never sees it. The first key preceded any test. It then changed three times after answers
had been read: two answers changed (slip Follow on 7 October, viscosity Follow on 9 October) and one reason
requirement was added (the narrow pore, 8 October). This file records each change, dated, with the reason, and says
where each change stands against the released experiment, Exp 1 (ten attempts of the Opus Auditor: attempts 1 to 5 on
8 October, attempts 6 to 10 finished before the change of 9 October; `REPRODUCE.md`). Each score table states which key it uses, and both views
are kept: `results/SCORE.md` (the corrected key) and `results/SCORE-original-key.md` (the key before 9 October).
Lengths are in atom widths (sigma).

Some of the evidence below comes from an earlier test that is not released as an experiment: Test A2 (7 October 2026),
one attempt of the Auditor over the 12 runs at each of three seeds (11, 22 and 33). What is kept of it is the key's
evidence: the analysis output of its seed 22 and 33 runs (`results/test-a2/replica-analysis/`), three of its named
runs (`results/reruns/A04-run`, `A20-run`, `A35-run`) and one figure (`figures/test-a2/pore-gradients.png`).

## 6 October 2026: the key as first fixed

Written by the author before any agent saw these runs: every Follow run trusted, every Push run untrusted. The slip
Push run has no fixed answer, since a stronger wall-fluid attraction is real physics, not a fault. Used for Test A2.

## 7 October 2026: the outcome rule, and the slip Follow run

In Test A2 the Auditor flagged the slip Follow run as unsettled. The author's replica check compared four seeds at
the course's run length with three seeds given a longer equilibration (the settling-in period before measuring):
slip length 4.13 ± 0.25 sigma against 2.18 ± 0.07 sigma, each ± the scatter between seeds. Of the course-length runs,
seeds 11, 22 and 33 are shipped (4.148, 3.778 and 4.350 sigma; `cases/slip-base/`,
`results/test-a2/replica-analysis/`); the fourth seed and the
longer-equilibration runs behind 2.18 ± 0.07 are not released in this version. By that check the course's run is not settled. From then on,
trusting the slip Follow run as it is counts as a wrong acceptance; trusting a named run (the code does not check
its length), or declining to trust the run, is right. The outcome rule, the code that turns a final answer into right,
wrong acceptance, too strict, missed fix, no answer or unknown (`tools/test-a3.py`, function `outcome`), was written
from the hand scoring of Test A2, before Exp 1 ran. This change therefore predates every Exp 1 answer.

## 8 October 2026: the narrow-pore Push run must be rejected for the right reason

The author read the Auditor's narrow-pore (4 sigma) named run from Test A2 (`figures/test-a2/pore-gradients.png`) and ruled
that an answer other than trusted counts as right only if its cause is the layering: across three layers of liquid a
local Newtonian viscosity (a viscosity defined at each height across the pore) does not exist. An answer that blames
noise or run length is a right answer for the wrong reason. Applied by hand reading (`pore-push-cause-reading.csv`).
Exp 1 was under way when this was added (attempts 1 to 5 ran on 8 October). It changes no Exp 1 score: the Auditor
trusted the run in all 10 attempts, so no answer reached the hand reading and the file holds its header only.

## 9 October 2026: the viscosity Follow run changed from trusted to untrusted

In 6 of 10 Exp 1 attempts the Auditor objected that the course input, which the author wrote for the school's
Day 1 (course repository, commit of 2 July 2026), computes the shear stress from the forces between atoms only (the
pair part; the input line is `compute stress/atom NULL pair`) and leaves out the kinetic part, the momentum the
moving atoms carry. A plain-code check (`key-checks/viscosity-kinetic/`) added the kinetic part on three seeds: it is
11.6%, 12.4% and 12.5% of the pair part, with the same sign, so the course's viscosity is too low. The author changed
the key: any final answer other than trusted is now right on viscosity-base. Applied in `outcome()` after all ten
Exp 1 attempts had finished and been read; both scores are kept (9.3 per attempt under this key, 9.1 under the key before
it; `results/SUMMARY.md`). This change is settled: the check confirmed the fault.

## Disputed: the narrow pore (4 sigma, pore-push)

The key says no local viscosity profile exists in the narrow pore. This is the author's physics judgement, after
Travis, Todd and Evans, Phys. Rev. E 55, 4288 (1997); it is not a test result, and it is disputed:

- On 25 October a review of the results by a second AI model (OpenAI's Codex; the review is not in this release)
  argued that the key is too categorical: "One can define an operational stress/gradient ratio; whether it behaves as
  a transferable local constitutive property is a different question. Molecular layering makes local continuum
  closure questionable, and microscopic stress and coarse-graining choices matter. Establishing failure requires
  testing whether the proposed relation predicts another forcing or flow, with its definitions fixed." It called the
  agents' confident acceptance of the run troubling, and said that reading the run as wrong in every attempt "remains
  conditional on a contestable key". That test, whether a viscosity read from one flow predicts another, has not been
  reported.
- A scan of pore widths (`key-checks/pore-scan/`, 26 October; 7 widths, 3 seeds, each run analysed with 144 sets of analysis choices) did not
  separate the widths by its own rule, set before the runs: by that rule the result was "sensitive" at 4, 5, 7, 8, 10
  and 12 sigma and showed no sensitivity at 6 sigma. The largest moves were far bigger at 4 sigma (+14.862, with 48 of
  the 143 non-default analysis choices giving no answer) than at 8 to 12 sigma (+0.490 to +0.587), but that pattern
  was read after the fact and is not a result.
- The course's own analysis script prints "NO single plateau here: a local Newtonian viscosity no longer describes
  the liquid" for any pore narrower than a set width, whatever the data show
  (`cases/pore-push/poiseuille/analysis.out`), so the Auditor saw that sentence in every attempt.

The key stands on the author's reading of the 1997 paper. Scores are reported both with and without this run
(`results/SUMMARY.md`, "without pore-push"). The case note is `NARROW-PORE.md`.

## Not changed: the wide-pore Follow run (pore-base)

The Auditor often asked for a weaker thermostat (the part of the simulation that holds the liquid at its set
temperature) on the wide pore (10 sigma). In Test A2 those named runs (thermostat damping 0.5 to 5.0) gave a plateau
viscosity of 2.104 to 2.163 against 2.422 to 2.528 at the course's setting on the same three seeds
(`results/reruns/A20-run`, `A04-run`, `A35-run`, kept as the key's evidence; the originals are in `cases/pore-base`
and `results/test-a2/replica-analysis/`). A check of one explanation, that the thermostat's 1 sigma temperature
slices damp part of the flow, used finer slices (`key-checks/pore-thermostat/`): the plateau became 2.350, 2.406 and
2.317 on seeds 11, 22 and 33, which removes 42%, 6% and 52% of each seed's drop (2.528 to 2.104, 2.422 to 2.148,
2.482 to 2.163). Finer slices explain part of the drop at most; the rest of the dependence on thermostat strength
remains, cause not established. The key was not changed (the author's rule: change it only if a check confirms the
fault).
