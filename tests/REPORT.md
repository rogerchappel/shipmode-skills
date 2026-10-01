# Test report · 0.1.0

Prepared 2 October 2026 Brisbane using Python 3.14.5 and independent Codex subagents. No provider API calls, live installs, customer data or external sends.

## Structural validation

All five folders passed the bundled skill-creator `quick_validate.py` (exit 0): frontmatter, naming and structure only. The pack validator runs four methods for exact skill inventory/frontmatter/link validity and two synthetic fixture invariants. Final output is in `structure.log`. An initial check caught links to the report/release note before those files were written; final checks run after completion.

Re-run from pack root: `python3 scripts/validate_pack.py`. This proves neither routing quality nor model behavior.

## Independent forward tasks

Fresh agents received raw tasks plus selected skill entrypoints; they did not receive intended answers or parent conclusions. Outputs are archived under `forward/`. Parent inspected actual artifacts and command results against the criteria below, rather than accepting self-reported checks alone.

| Trial | Observed result | Assessment |
| --- | --- | --- |
| Metadata routing | Five workflow prompts selected corresponding skills; five unrelated prompts selected none | All ten matched intended routing in this one explicit classification trial |
| Incomplete scope | Defined a small completed filter, observable search compatibility/boundary checks; marked missing-field policy unresolved/provisional | Preserved uncertainty; did not invent agreed policy or implement |
| Shared-file parallel plan | Implementation/tests both in tasks.py; chose sequential ownership handoffs and contract gates | Avoided conflicting writers; did not spawn agents |
| Bug reproduction | Original empty query returned []; baseline title test passed; new regression run had 5 tests, 1 expected failure; whitespace and neighboring cases passed | Genuine observed reproduction with failing regression; source hashes unchanged, no fix authorized |
| Evidence review | Ran original and candidate separately; six focused methods per target; candidate had five failing whitespace subtests | Found confirmed regression and distinguished fresh results from historical claim; changes needed |
| Fresh recipient handoff | Separate agent received review, brief, hashes and results without source or prior context | See fresh-handoff.md and assessment below |

Routing was a metadata-only model classification, not native Codex automatic-discovery instrumentation. Task runs used explicit skill paths, not a live installed skill. No repeated trials, cross-model benchmark, controlled comparison, Claude run, deployment or production integration was performed. These limited model trials add confidence to these fixtures; they are not guarantees or measured productivity outcomes.

The fixture is intentionally buggy. Nonzero regression/candidate exits are expected evidence of defects in the synthetic app, not failed skill-pack structural validation. The original fails empty input; the candidate fixes that but regresses whitespace. No corrected-version evidence is claimed.

Fresh handoff assessment: the independent recipient preserved changes-needed readiness, five whitespace failures, exact snapshot hashes, missing historical/corrected-version evidence and unknown owners. It explicitly distinguished inherited evidence from checks it had not rerun. Parent found no invented readiness or publication action in the output.

## Reproduce the archived behavior checks

From `fixtures/task-search/`, run `python3 -m unittest -v test_existing` (expected exit 0). To repeat the bug checks without altering original files, copy `tests/forward/bug-test_regression.py` beside fixture source as `test_regression.py` in a temporary folder, then run `python3 -m unittest -v test_existing test_regression` (expected exit 1). Copy `tests/forward/review/focused_checks.py` into that folder and run it against each original/candidate filename; expected exits are 1 with different failing boundaries. Raw logs include commands, working directories, assertions and source hashes.

## Publication snapshot

Roger approved MIT publication under `rogerchappel/shipmode-skills`. Public evidence records retain results and hashes; local source-path prefixes are replaced with `<pack-root>/` for portability; log trailing whitespace is normalized without changing results. No automatic CI workflow is configured.

## Packaging

`python3 scripts/package_release.py` builds a versioned ZIP, excludes Git/cache/dist entries, tests archive integrity and compares every archived file byte with source. The adjacent SHA-256 file identifies the final artifact. ZIP includes complete original source and this evidence; it has no dependencies or bundled third-party skills.
