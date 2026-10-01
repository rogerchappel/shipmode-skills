# Example: completed filter

Shared contract: `filter_tasks(tasks, *, completed=None)` returns a new list of original task objects; `None` means all, booleans select exact values. No storage change.

| Workstream | Writes | Depends on | Artifact/check |
| --- | --- | --- | --- |
| Function owner | `tasks.py` | Agreed contract | Predicate implementation; run existing checks |
| Test owner | `test_tasks.py` | Agreed contract | None/True/False/empty/non-mutation cases; new tests may fail until integration |
| Integration owner | `README.md` | Function and tests | Usage example; run combined suite |

If the repository keeps tests in `tasks.py`, parallel edits conflict: choose sequential work or move tests only with scope agreement. Do not spawn agents merely because this example mentions owners.
