# Task search handoff

**Readiness: changes needed; not ready for release or acceptance of the stated brief.** The candidate fixes empty-query behavior in the supplied focused run, but whitespace-only queries still return no tasks. No fix was made in this handoff, and nothing was published.

Scope is a Python standard-library synthetic title-search function: empty and whitespace-only queries must show all tasks without changing the input; nonblank queries use case-insensitive substring matching. The brief states there is no UI, storage, network, or real user data.

Evidence covers the copied snapshot recorded in [manifest.json](/tmp/shipmode-review-trial/manifest.json), not an identified commit or release version. Recorded SHA-256: candidate `1c44f6c7de0dde83ceb2571f29757f35fdd7bd846920501fb9f7b3b3e42c946f`; original `39efca635c2423355e181c232abff4ee77a38e1f83b0b906f29720c6dd4674ab`. I read only the supplied brief, review, manifest, and results; I did not inspect source, verify hashes independently, or rerun checks.

Recorded checks, all in `/tmp/shipmode-review-trial` (runner identity unknown):

| Command | Recorded outcome |
| --- | --- |
| `python3 -m unittest -v test_existing.py` | Exit 0; one original title-match assertion passes. The review says this imports the original, so it does not establish candidate readiness. |
| `python3 focused_checks.py tasks.py` | Exit 1; six methods run, empty-query test fails. |
| `python3 focused_checks.py review_candidate.py` | Exit 1; six methods run, five whitespace subtests fail; the other five methods pass. |

To reproduce, use the candidate command above from that directory. According to [review.md](/tmp/shipmode-review-trial/review.md), candidate lines 2–3 handle the empty query, while the normalized blank branch at lines 5–6 returns `[]`. The review identifies failing space, multiple-space, tab, newline, and mixed-whitespace cases. Passing candidate checks cover empty query, representative case-insensitive/Unicode substring matches and no-match, empty task list, padded nonblank query, and unchanged synthetic input contents/record identities.

The historical claim “The original title-match check passed” has no historical command, log, status, or hash. The fresh original-only pass is separate evidence. The review reports an orchestration exit of 0 because failures were captured; the individual recorded test exits of 1 remain failures. [results.json](/tmp/shipmode-review-trial/results.json) contains the commands and captured outputs.

Known limits: no broader integration, security, UI, storage, network, deployment, or publication validation is supplied; platform/runtime versions and supported platforms are unspecified. Results cover representative synthetic list/dict cases only. No release version, package/artifact list, licence/content approval, rollback/uninstall procedure, or owners are supplied. Reverting to the original would retain its demonstrated empty-query defect.

Next action (owner unknown): correct the candidate's whitespace behavior, rerun the focused candidate checks against the corrected exact snapshot, and record its identity and outcomes before reassessing readiness. Public-release requirements and ownership remain unresolved. Publication is explicitly unauthorized.
