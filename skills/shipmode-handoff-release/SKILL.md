---
name: shipmode-handoff-release
description: Prepare a concise developer handoff or release-readiness summary from changes and verification evidence with known limits and next actions; use at a work boundary, not to deploy.
---

# Prepare a handoff

Give the next person enough verified context to continue or decide on a release.

1. Read the agreed scope, changed artifacts, verification records, and open issues. Identify the revision or file snapshot the evidence covers.
2. State delivered behavior and how to try it. Link to concrete files or commands; separate completed work from proposals.
3. Summarize checks with commands/results and who ran them. Carry forward failures, missing checks, unsupported platforms, and unresolved assumptions.
4. State readiness for the specific target (review, internal trial, or public release). Name blockers and the next owner/action where known. If ownership is unknown, say so rather than assigning someone.
5. Include rollback/uninstall guidance when relevant and known. For a release, list version and artifacts plus content/licence approval still needed. Never infer publication authorization from technical readiness.

Return outcome, usage, evidence, known limits, readiness, and next actions in a short note. This workflow does not merge, send, publish, or deploy.

Read [example.md](example.md) for a handoff with a passing suite and an unresolved boundary.
