import unittest
import gcd_problem_2


class TestGreatestCommonDivisor(unittest.TestCase):
    def test_gcd_15_20(self):
        result = gcd_problem_2.greatest_common_divisor(15, 20)
        self.assertEqual(result, 5)

    def test_gcd_40_200(self):
        result = gcd_problem_2.greatest_common_divisor(40, 200)
        self.assertEqual(result, 40)

    def test_gcd_same_numbers(self):
        result = gcd_problem_2.greatest_common_divisor(10, 10)
        self.assertEqual(result, 10)

    def test_gcd_coprime(self):
        result = gcd_problem_2.greatest_common_divisor(7, 13)
        self.assertEqual(result, 1)

    def test_gcd_one_is_divisor(self):
        result = gcd_problem_2.greatest_common_divisor(5, 25)
        self.assertEqual(result, 5)

    def test_gcd_large_numbers(self):
        result = gcd_problem_2.greatest_common_divisor(48, 18)
        self.assertEqual(result, 6)

    def test_gcd_reversed_order(self):
        result = gcd_problem_2.greatest_common_divisor(20, 15)
        self.assertEqual(result, 5)

    def test_gcd_with_one(self):
        result = gcd_problem_2.greatest_common_divisor(1, 100)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
