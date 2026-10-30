"""The released experiment and its tries: one list, read by test-a3.py and tables.py.
Historical: these names score the shipped answers and are checked by tools/check.py. A new try goes in a separate
results folder (TESTBED_RESULTS) and is scored with `tools/test-a3.py score --tries <names>`; it is never added here."""

HISTORICAL = {  # name: (the Auditor's model, the tries)
    "Exp 1": ("claude-opus-5-5", [f"exp1r{r}" for r in range(1, 11)]),  # the reference Auditor
}
LABELS = {"Exp 1": "Exp 1 (Opus, base)"}


def full_twelve():
    """{name: tries} for the experiments that judged all 12 runs."""
    return {name: tries for name, (_, tries) in HISTORICAL.items()}
