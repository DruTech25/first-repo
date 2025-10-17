import unittest

from app.strings import concat_strings


class TestStrings(unittest.TestCase):
    def test_concat_strings_mixed_types(self):
        self.assertEqual(concat_strings(["a", "b", 3, None]), "ab3None")

    def test_concat_strings_empty(self):
        self.assertEqual(concat_strings([]), "")


if __name__ == "__main__":
    unittest.main()
