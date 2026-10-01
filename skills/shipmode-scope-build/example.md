# Example: local task list

Request: “Add a completed filter to our in-memory task list. Keep it small.”

Output sketch:
- Outcome: callers can request only completed tasks without changing storage.
- Include: an optional `completed` argument; defer UI, persistence, accounts.
- Assumption: `None` keeps current behavior; `True`/`False` filters exact booleans.
- Check: with one complete and one incomplete task, `completed=True` returns only the complete one.
- Boundary: no matching tasks returns `[]`; the input list is unchanged.
- Sequence: confirm public function signature, implement predicate, add checks, run existing tests.

These are acceptance proposals, not execution evidence.
