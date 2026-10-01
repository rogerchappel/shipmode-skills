import copy
import unittest

from tasks import search_tasks


class SearchRegressionTests(unittest.TestCase):
    def setUp(self):
        self.tasks = [{"title": "Ship demo"}, {"title": "Write notes"}]

    def test_empty_query_returns_all_tasks_without_mutation(self):
        before = copy.deepcopy(self.tasks)
        actual = search_tasks(self.tasks, "")
        self.assertEqual(self.tasks, before)
        self.assertEqual(actual, before)

    def test_whitespace_query_returns_all_tasks_without_mutation(self):
        before = copy.deepcopy(self.tasks)
        actual = search_tasks(self.tasks, " \t\n ")
        self.assertEqual(self.tasks, before)
        self.assertEqual(actual, before)

    def test_nonblank_query_keeps_case_insensitive_substring_filter(self):
        before = copy.deepcopy(self.tasks)
        self.assertEqual(search_tasks(self.tasks, "  HIP  "), self.tasks[:1])
        self.assertEqual(self.tasks, before)

    def test_unmatched_query_returns_no_tasks(self):
        self.assertEqual(search_tasks(self.tasks, "missing"), [])


if __name__ == "__main__":
    unittest.main()
