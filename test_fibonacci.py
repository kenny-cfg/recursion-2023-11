import unittest

from fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):
    def test_first_seven_are_correct(self):
        expected = [0, 1, 1, 2, 3, 5, 8]

        actual = [fibonacci(x) for x in range(7)]

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
