---
name: shipmode-scope-build
description: Scope a small software build into a bounded slice with observable acceptance checks before implementation; use for vague feature briefs, not debugging or code review.
---

# Scope a small build

Turn a feature brief into the smallest useful deliverable the user can assess.

1. Read the brief and relevant existing behavior. Separate stated requirements from assumptions. Preserve explicit constraints; ask only when a missing decision changes the slice materially.
2. Describe one end-to-end user outcome. Name what is included and what is deferred; do not turn a small feature into a platform.
3. Define observable acceptance checks: starting state, action/input, expected result, and how to verify it. Include a meaningful boundary or failure case. Avoid checks such as “works correctly.”
4. Connect the checks to a short implementation sequence and any dependency that can block it. State unresolved questions and reasonable provisional choices.

Return a compact build brief with outcome, scope/deferred work, assumptions, checks, and next steps. A proposed check is not a passed test. Do not implement unless the user's task includes implementation.

For a concrete sample, read [example.md](example.md).
