# Example: handoff to review

Delivered: empty-query search returns all tasks in `tasks.py`.
Try: call `search_tasks([{ "title": "Ship" }], "")`.
Evidence: empty-query and existing title checks pass on the supplied snapshot.
Limit: whitespace-only query is a stated requirement but still fails; no UI exists.
Readiness: changes needed before calling this complete.
Next: fix whitespace handling, rerun both boundaries and existing suite, then request review. Owner not yet assigned.

A passing subset is not permission to release.
