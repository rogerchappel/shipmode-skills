# Synthetic task search

Python standard library only. No UI, storage, network or real user records.
Existing `tasks.py` implements title search. The requirement is that empty and whitespace-only queries show all tasks, without mutating the input. Nonblank search is case-insensitive substring matching.

For bug work, use `tasks.py` and `test_existing.py`. For review, compare `tasks.py` with `review_candidate.py`. The supplied historical claim is: “The original title-match check passed.” Verify its relevance yourself; it is not a current candidate run.
