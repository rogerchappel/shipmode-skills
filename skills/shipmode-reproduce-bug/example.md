# Example: empty search

Report: blank search should show all tasks. `search_tasks(tasks, "")` returns `[]`.

Reproduction: two synthetic tasks, query `""`; expected both tasks, actual none.
Regression: assert the returned list equals both tasks. Neighbor: query `"ship"` returns only a title containing “ship”. Add whitespace-only query if the requirement treats it as blank.

Run the check before the patch. Record an assertion failure as evidence, not as a harness failure. After a fix, record command, exit status and results; keep baseline tests too.
