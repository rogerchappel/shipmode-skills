# Example: blank-query patch

Requirement: empty and whitespace-only searches return all tasks.
Patch: changes `if not query` to return all tasks, but trims query later.
Supplied log: existing “ship” search test passed before the patch.

Useful review: supplied log is stale and misses blank input. Run empty and whitespace checks on the patch. If whitespace returns `[]`, report that confirmed defect with its condition; separate it from the stale-log gap. Do not describe this patch as verified because the old happy path passed.
