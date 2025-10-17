import unittest

from app.utils import build_grep_command


class TestSecurity(unittest.TestCase):
    def test_build_grep_command_returns_argv_and_sanitizes(self):
        # Expect a list argv and no shell metacharacters allowed
        safe_query = "hello world"
        argv = build_grep_command(safe_query)
        # The fixed behavior: list argv with '--' to terminate options
        self.assertIsInstance(argv, list)
        self.assertEqual(["grep", "-R", "--", safe_query, "."], argv)

    def test_build_grep_command_rejects_injection(self):
        with self.assertRaises(ValueError):
            build_grep_command("foo; rm -rf /")
        with self.assertRaises(ValueError):
            build_grep_command("$(whoami)")
        with self.assertRaises(ValueError):
            build_grep_command("bad|pipe")


if __name__ == "__main__":
    unittest.main()
