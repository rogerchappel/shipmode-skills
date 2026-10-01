"""Offline structure and synthetic behavior checks; no model evaluation."""
from pathlib import Path
import importlib.util
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"shipmode-scope-build", "shipmode-plan-parallel", "shipmode-reproduce-bug", "shipmode-review-evidence", "shipmode-handoff-release"}

class PackChecks(unittest.TestCase):
    def test_skill_structure(self):
        paths = list((ROOT / "skills").glob("*/SKILL.md"))
        self.assertEqual({p.parent.name for p in paths}, EXPECTED)
        for p in paths:
            text = p.read_text()
            self.assertTrue(text.startswith("---\n"), p)
            front, body = text[4:].split("\n---\n", 1)
            fields = dict(line.split(": ", 1) for line in front.splitlines())
            self.assertEqual(set(fields), {"name", "description"})
            self.assertEqual(fields["name"], p.parent.name)
            self.assertRegex(fields["name"], r"^[a-z0-9-]{1,63}$")
            self.assertGreater(len(fields["description"]), 40)
            self.assertLess(len(body.split()), 300)
            for target in re.findall(r"\]\(([^)]+)\)", body):
                self.assertTrue((p.parent / target).is_file(), target)
    def test_root_links(self):
        for target in re.findall(r"\]\(([^)]+)\)", (ROOT / "README.md").read_text()):
            if not target.startswith("https://"):
                self.assertTrue((ROOT / target).is_file(), target)
    def test_fixture_has_real_boundary_failure(self):
        spec = importlib.util.spec_from_file_location("fixture", ROOT / "fixtures/task-search/tasks.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        tasks = [{"title": "Ship demo"}, {"title": "Write notes"}]
        self.assertEqual(module.search_tasks(tasks, "SHIP"), tasks[:1])
        self.assertEqual(module.search_tasks(tasks, ""), [])
        self.assertNotEqual(module.search_tasks(tasks, ""), tasks)
    def test_candidate_has_distinct_gap(self):
        spec = importlib.util.spec_from_file_location("candidate", ROOT / "fixtures/task-search/review_candidate.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        tasks = [{"title": "Ship demo"}]
        self.assertEqual(module.search_tasks(tasks, ""), tasks)
        self.assertNotEqual(module.search_tasks(tasks, "  "), tasks)

if __name__ == "__main__":
    unittest.main(verbosity=2)
