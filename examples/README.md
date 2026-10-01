# Example index

| Goal | Prompt | Inputs |
| --- | --- | --- |
| Small scope | `$shipmode-scope-build Scope a completed filter for this in-memory task list. Give acceptance checks; do not implement.` | `fixtures/task-search/brief.md`; assume tasks also have a boolean completed field |
| Parallel plan | `$shipmode-plan-parallel Plan a completed filter with function, tests and documentation owners. Do not spawn agents.` | Scope example; `tasks.py`, `test_existing.py`, a proposed `README.md` |
| Reproduction | `$shipmode-reproduce-bug Reproduce blank search returning no tasks and add a regression check. Do not fix source.` | Task-search fixture |
| Evidence review | `$shipmode-review-evidence Assess this candidate against the stated search requirements and supplied historical claim.` | Fixture brief, original and candidate |
| Handoff | `$shipmode-handoff-release Prepare a review handoff for this search patch. Include known limits; do not publish.` | Candidate plus actual focused-check evidence |

Each skill has a short `example.md`. Examples illustrate expected decisions, not mandatory wording. The intentionally buggy fixture is for isolated practice; copy it into a temporary folder before edits.
