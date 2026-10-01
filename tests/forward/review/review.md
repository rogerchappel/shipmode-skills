# Search candidate review

## Findings

**Changes needed: whitespace-only queries hide all tasks.** In `review_candidate.py:5-6`, the normalized blank branch returns `[]`. With a nonempty input and query `" "`, `"   "`, `"\\t"`, `"\\n"`, or mixed whitespace, all tasks are required but no tasks are returned. This also regresses the original whitespace behavior. Reproduce using `python3 focused_checks.py review_candidate.py` from this directory; five whitespace subtests fail. The empty-query fix at lines 2-3 passes.

## Requirements and evidence

| Requirement | Candidate path | Observed candidate check | Gap |
| --- | --- | --- | --- |
| Empty query shows all tasks | lines 2-3 | `test_empty_shows_all` passes | None for tested list input |
| Whitespace-only query shows all tasks | lines 4-6 | `test_whitespace_shows_all` fails for space, multiple spaces, tab, newline, mixed whitespace | Confirmed defect |
| Input is not mutated | all return paths | `test_inputs_unchanged` passes across empty, whitespace, matching and no-match queries; checks nested contents and record identities | Synthetic list/dict inputs only |
| Nonblank case-insensitive substring matching | lines 4, 7 | `test_case_insensitive_substring` passes uppercase substring, ordinary substring, Unicode casefold and no-match cases | Representative cases only |
| Empty task list | all branches | `test_empty_task_input` passes | Additional boundary check |
| Padded nonblank query | lines 4, 7 | `test_padded_nonblank` passes | Additional check of existing strip behavior |

## Evidence provenance

The brief supplies only a historical claim that the original title-match check passed, with no historical command, exit status, log or source hash. It is not candidate evidence. A fresh run of copied `test_existing.py` imports copied original `tasks.py`; it passes one title-match assertion (exit 0), establishing only that original check now. Fresh focused runs explicitly load each filename: original exits 1 because the empty-query check fails; candidate exits 1 because five whitespace subtests fail. Both run six test methods. The candidate passes the other five methods.

`manifest.json` records SHA-256 hashes and original source path for untouched copied inputs; `diff.log` records the before/after diff; `focused_checks.py` contains assertions; `check-1.log` through `check-3.log` and `results.json` preserve commands, working directory, results and exit statuses. The runner captures failures, so its orchestration process exited 0; the preserved individual test exits are authoritative.

## Recommendation

**Do not call this ready. Changes needed** for the stated brief because the candidate fails an explicit acceptance requirement. Code was not fixed. Readiness after a correction remains unverified: rerun focused candidate checks against the corrected exact version and record that version. No broader integration, security, storage, UI, network, merge, deployment or publication evidence is claimed; the brief describes a standard-library synthetic function only.
