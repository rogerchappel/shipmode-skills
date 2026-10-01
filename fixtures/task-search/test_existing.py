import unittest
from tasks import search_tasks

class ExistingTests(unittest.TestCase):
    def test_title_match(self):
        tasks = [{"title": "Ship demo"}, {"title": "Write notes"}]
        self.assertEqual(search_tasks(tasks, "SHIP"), tasks[:1])

if __name__ == "__main__":
    unittest.main()
