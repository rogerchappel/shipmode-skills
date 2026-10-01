import copy
import importlib.util
import sys
import unittest

filename = sys.argv.pop(1)
spec = importlib.util.spec_from_file_location("review_target", filename)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
search_tasks = module.search_tasks

class FocusedChecks(unittest.TestCase):
    def setUp(self):
        self.tasks = [{"title": "Ship demo", "id": 1}, {"title": "Write notes", "id": 2}, {"title": "Straße checklist", "id": 3}]
    def test_empty_shows_all(self):
        self.assertEqual(search_tasks(self.tasks, ""), self.tasks)
    def test_whitespace_shows_all(self):
        for query in [" ", "   ", "\t", "\n", " \t\n "]:
            with self.subTest(query=repr(query)):
                self.assertEqual(search_tasks(self.tasks, query), self.tasks)
    def test_case_insensitive_substring(self):
        for query, expected in [("HIP", self.tasks[:1]), ("notes", self.tasks[1:2]), ("STRASSE", self.tasks[2:]), ("absent", [])]:
            with self.subTest(query=query):
                self.assertEqual(search_tasks(self.tasks, query), expected)
    def test_padded_nonblank(self):
        self.assertEqual(search_tasks(self.tasks, "  sHiP  "), self.tasks[:1])
    def test_inputs_unchanged(self):
        for query in ["", " ", "\t\n", "SHIP", "absent"]:
            with self.subTest(query=repr(query)):
                snapshot=copy.deepcopy(self.tasks)
                identities=[id(task) for task in self.tasks]
                search_tasks(self.tasks,query)
                self.assertEqual(self.tasks,snapshot)
                self.assertEqual([id(task) for task in self.tasks],identities)
    def test_empty_task_input(self):
        for query in ["", " ", "SHIP"]:
            self.assertEqual(search_tasks([], query), [])

if __name__ == "__main__":
    unittest.main(verbosity=2)
