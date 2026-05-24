import unittest

import os
import tempfile

from repo_onboard_ai.__main__ import command_hints, repo_data, tree_lines, walk_repo


class RepoOnboardTest(unittest.TestCase):
    def test_command_hints_for_python_project(self):
        hints = dict(command_hints(["pyproject.toml", "README.md"]))
        self.assertEqual(hints["Install"], "python3 -m pip install -e .")
        self.assertEqual(hints["Test"], "python3 -m unittest discover -s tests")

    def test_repo_data_shape(self):
        data = repo_data("/tmp/example", ["pyproject.toml", "src/app.py", "README.md"])
        self.assertEqual(data["repo_name"], "example")
        self.assertTrue(data["command_hints"])

    def test_tree_lines_groups_nested_files(self):
        lines = tree_lines(["README.md", "src/app.py", "src/lib/core.py"], max_depth=2)
        rendered = "\n".join(lines)
        self.assertIn("README.md", rendered)
        self.assertIn("src/", rendered)
        self.assertIn("app.py", rendered)

    def test_walk_repo_supports_extra_ignore_dirs(self):
        with tempfile.TemporaryDirectory() as repo:
            os.mkdir(os.path.join(repo, "generated"))
            with open(os.path.join(repo, "generated", "skip.py"), "w", encoding="utf-8") as handle:
                handle.write("pass")
            with open(os.path.join(repo, "keep.py"), "w", encoding="utf-8") as handle:
                handle.write("pass")
            files = walk_repo(repo, 20, extra_ignore=["generated"])
        self.assertEqual(files, ["keep.py"])


if __name__ == "__main__":
    unittest.main()
