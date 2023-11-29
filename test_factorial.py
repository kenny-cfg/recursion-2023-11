import unittest

from factorial import factorial


class TestFactorial(unittest.TestCase):
    def test_first_seven_factorials_are_correct(self):
        expected = [1, 1, 2, 6, 24, 120, 720]

        actual = [factorial(x) for x in range(7)]

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
