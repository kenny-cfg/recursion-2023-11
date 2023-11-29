import unittest

from fibonacci import fibonacci, fibonacci_doubled, fibonacci_without_recursion


class TestFibonacci(unittest.TestCase):
    def test_first_seven_are_correct(self):
        expected = [0, 1, 1, 2, 3, 5, 8]

        actual = [fibonacci(x) for x in range(7)]

        self.assertEqual(actual, expected)

    def test_first_seven_are_correct_for_doubled(self):
        expected = [0, 1, 1, 2, 3, 5, 8]

        actual = [fibonacci_doubled(x) for x in range(7)]

        self.assertEqual(actual, expected)

    def test_first_seven_are_correct_for_non_recursive_version(self):
        expected = [0, 1, 1, 2, 3, 5, 8]

        actual = [fibonacci_without_recursion(x) for x in range(7)]

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
