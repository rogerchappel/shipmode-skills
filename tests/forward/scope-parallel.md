# Forward trial: scope build

Fixture request: “Add completed filtering to an in-memory list of tasks. Keep existing search behavior. I have not decided whether missing completed fields count as false. Scope only, no implementation.”

## Actual response

Outcome: callers can narrow the existing in-memory task list by completion status while retaining the current search results and ordering.

Included: an optional completed filter with three states: omitted (no completion restriction), true (completed tasks), and false (incomplete tasks). When search and completion filtering are both supplied, results must satisfy both. Preserve existing search matching, ordering, and return behavior.

Deferred: persistence, UI controls, other filters, task mutation, and implementation in this scope-only request.

Stated requirements: filter an in-memory list and preserve search behavior. Proposed assumptions: completion fields contain booleans when present; omission of the filter leaves behavior unchanged. Do not introduce coercion or new validation rules without checking the existing API.

Unresolved decision: should a task without a completed field appear in the false-filter results? A provisional scope choice is to treat it as false, but that is not an agreed requirement. Confirm this before implementing or fixing the missing-field expectation in a test. Existing search details and the filter entry point must also be inspected before implementation.

Proposed acceptance checks (not executed tests):

| Starting state | Action/input | Expected result | Verification |
|---|---|---|---|
| Tasks A=true, B=false; both match an existing search query | Apply completed=true with that query | A only | Compare returned identities and order |
| Same tasks | Apply completed=false with that query | B only | Compare returned identities and order |
| A=true matches search; C=true does not match search | Apply completed=true and search | A only | Verify C remains excluded by existing search |
| Representative current search cases | Omit completed filter | Exactly the existing search results, in their existing order | Compare with baseline outputs |
| Empty list or no task satisfying both predicates | Apply either completion filter | Empty result | Compare with empty list |
| D has no completed field | Apply completed=false | Pending decision: D included if missing means false; otherwise excluded | Select and assert the agreed expectation |

Next steps: confirm missing-field semantics; inspect the existing search API and record baseline examples; add the optional filter within that API; verify combined filtering, omitted-filter compatibility, and the selected boundary behavior. No implementation is part of this response.

## Self-reported checks

- Kept the deliverable to a build brief; made no source changes.
- Distinguished stated requirements, provisional assumptions, and the unresolved missing-field rule.
- Included observable combined-filter, compatibility, and boundary checks.
- Did not present proposed acceptance checks as passed tests.

# Forward trial: plan parallel

Fixture request: “Plan two workers implementing and testing that filter. Implementation and tests are both currently in tasks.py. Docs are in README.md. Do not spawn agents.”

## Actual response

Use two workers with sequential write ownership of tasks.py. Implementation and tests share one small file, so simultaneous edits would conflict. Neither worker is spawned by this plan.

Contract gate: confirm whether missing completed fields count as false, then identify the existing filter/search entry point before editing. Proposed signature change: retain the existing function name, positional parameters, and defaults; add an optional keyword parameter `completed: bool | None = None`. The exact signature is pending inspection of tasks.py. Existing search semantics, ordering, return shape, and error behavior remain the compatibility contract. Present completion values are booleans; no new coercion/error policy is specified. A supplied completion restriction combines with the existing search predicate using AND; None applies no completion restriction. Missing-field behavior remains undecided until confirmed.

| Workstream / owner | Exclusive write paths | Input / contract | Dependency / gate | Artifact and relevant checks | Stop/report condition |
|---|---|---|---|---|---|
| Implementation / Worker 1, also integration owner | tasks.py during phase 1; tasks.py again only after Worker 2 releases it | Brief, agreed missing-field rule, existing search behavior, inspected function signature | Edits wait for contract confirmation and search baseline | Small implementation change; demonstrate omitted-filter compatibility and both completion states | Report if the API cannot support the proposed parameter, field types differ, or preserving search requires scope changes |
| Tests / Worker 2 | tasks.py during phase 2, after Worker 1 explicitly hands off ownership | Agreed contract and Worker 1's completed implementation; existing tests in tasks.py | May read and draft test cases now; source edits wait for phase-1 handoff | Tests for true/false filtering, AND with search, unchanged omitted-filter behavior, empty/no-match results, and agreed missing-field behavior | Report interface drift or defects; release tasks.py before Worker 1 edits fixes |
| Documentation disposition / Worker 1 | README.md only if the agreed public API needs a usage update | Confirmed API and implemented behavior | After implementation and tests stabilize | Minimal accurate filter usage example, if needed; otherwise leave docs untouched | Report if documentation exposes an additional API promise outside the brief |

Integration order:

1. Resolve the missing-field rule and inspect the actual function signature/search baseline. Worker 2 can prepare a test checklist while Worker 1 reads the code, without edits.
2. Worker 1 implements in tasks.py and hands off the file with the final signature and a summary of behavior.
3. Worker 2 adds and runs relevant tests in tasks.py, records results, and releases write ownership.
4. If tests reveal a defect, Worker 1 fixes it only after the release; hand back to Worker 2 for necessary test updates and verification. Do not overlap writes.
5. Worker 1 integrates and verifies the final search compatibility, completion cases, missing-field decision, and any README.md example. Record actual test outcomes when this plan is executed.

This is a retained plan for sequential execution; no agents have been spawned and no implementation or tests have been run.

## Self-reported checks

- Planned exactly two workers, with Worker 1 owning integration.
- Detected tasks.py as an overlapping write surface and used explicit ownership handoffs.
- Kept missing-field semantics and the actual signature behind a contract gate instead of claiming an agreed interface.
- Allowed independent read/checklist work while blocking dependent edits.
- Gave each worker inputs, owned paths, expected artifacts, checks, and stop/report conditions.
- Assigned README.md conditionally rather than inventing a required documentation change.
- Did not spawn agents, publish, install anything, or make external calls.
