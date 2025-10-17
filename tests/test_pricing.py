import unittest

from app.pricing import calculate_discount


class TestPricing(unittest.TestCase):
    def test_calculate_discount_basic(self):
        self.assertAlmostEqual(calculate_discount(200.0, 10.0), 180.0)
        self.assertAlmostEqual(calculate_discount(100.0, 0.0), 100.0)
        self.assertAlmostEqual(calculate_discount(100.0, 100.0), 0.0)

    def test_calculate_discount_invalid_percent(self):
        for percent in (-5.0, 150.0):
            with self.assertRaises(ValueError):
                calculate_discount(100.0, percent)


if __name__ == "__main__":
    unittest.main()
