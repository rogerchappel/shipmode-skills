# Actual execution evidence

Runtime: Python 3.14.5. Test/reproduction working directory: `/tmp/shipmode-bug-trial`.

Command: `python3 reproduce.py`

Exit status: 0

```text
query='' expected=[{'title': 'Ship demo'}, {'title': 'Write notes'}] actual=[] matches=False
query=' \t\n ' expected=[{'title': 'Ship demo'}, {'title': 'Write notes'}] actual=[{'title': 'Ship demo'}, {'title': 'Write notes'}] matches=True
query='SHIP' expected=[{'title': 'Ship demo'}] actual=[{'title': 'Ship demo'}] matches=True
query='missing' expected=[] actual=[] matches=True
```

Command: `python3 -m unittest -v test_existing test_regression`

Exit status: 1

```text
test_title_match (test_existing.ExistingTests.test_title_match) ... ok
test_empty_query_returns_all_tasks_without_mutation (test_regression.SearchRegressionTests.test_empty_query_returns_all_tasks_without_mutation) ... FAIL
test_nonblank_query_keeps_case_insensitive_substring_filter (test_regression.SearchRegressionTests.test_nonblank_query_keeps_case_insensitive_substring_filter) ... ok
test_unmatched_query_returns_no_tasks (test_regression.SearchRegressionTests.test_unmatched_query_returns_no_tasks) ... ok
test_whitespace_query_returns_all_tasks_without_mutation (test_regression.SearchRegressionTests.test_whitespace_query_returns_all_tasks_without_mutation) ... ok

======================================================================
FAIL: test_empty_query_returns_all_tasks_without_mutation (test_regression.SearchRegressionTests.test_empty_query_returns_all_tasks_without_mutation)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/private/tmp/shipmode-bug-trial/test_regression.py", line 15, in test_empty_query_returns_all_tasks_without_mutation
    self.assertEqual(actual, before)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [] != [{'title': 'Ship demo'}, {'title': 'Write notes'}]

Second list contains 2 additional elements.
First extra element 0:
{'title': 'Ship demo'}

- []
+ [{'title': 'Ship demo'}, {'title': 'Write notes'}]

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=1)
```

Command: `shasum -a 256 shipmode-skills/fixtures/task-search/tasks.py /tmp/shipmode-bug-trial/tasks.py`

Exit status: 0

```text
39efca635c2423355e181c232abff4ee77a38e1f83b0b906f29720c6dd4674ab  shipmode-skills/fixtures/task-search/tasks.py
39efca635c2423355e181c232abff4ee77a38e1f83b0b906f29720c6dd4674ab  /tmp/shipmode-bug-trial/tasks.py
```
