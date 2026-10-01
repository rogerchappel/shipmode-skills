# Blank search reproduction

The reported failure is verified for `query=""` with two synthetic tasks. The requirement in `brief.md` says empty and whitespace-only queries must return all tasks without mutating the input. Expected: both tasks, in their input order. Actual: `[]`.

Setup: copied only `tasks.py`, `test_existing.py`, and `brief.md` from the task-search fixture into this fresh directory. Python 3.14.5; standard library only; no installation, network, or external actions.

Run `python3 reproduce.py` here for explicit inputs and expected/actual outputs (exit 0; this is a diagnostic script). Run `python3 -m unittest -v test_existing test_regression` for the regression (exit 1, one failure among five tests). Full actual output and unchanged-source hashes are in `evidence.md`.

The existing `python3 -m unittest -v test_existing` baseline passed one test, exit 0. It checks uppercase title matching and does not exercise blank input. The new `test_regression.py` checks empty and whitespace-only input, preservation of input values, trimmed mixed-case substring search, and an unmatched query. Only the empty-query check fails. These neighboring cases guard against a future fix that indiscriminately returns all tasks for every query.

Observed narrowing: empty string fails; whitespace containing spaces, tab, and newline passes. Nonblank `SHIP` and unmatched `missing` behave as required. Input values remain unchanged for the checked cases.

Suspected cause: `tasks.py` returns `[]` immediately for falsey queries, before stripping whitespace and matching titles. The empty string takes that branch; a nonempty whitespace string becomes an empty needle, which matches every title.

Source was not fixed. SHA-256 of both the original and copied `tasks.py`: `39efca635c2423355e181c232abff4ee77a38e1f83b0b906f29720c6dd4674ab`. There is no after-fix evidence because fixing was explicitly excluded.

Limits: synthetic standard-library function fixture only; no UI, storage, network, real records, or application integration was tested. Non-string queries, malformed records, and downstream mutation of returned records are outside the supplied requirement and were not tested. No blockers to reproduction or adding the check.
