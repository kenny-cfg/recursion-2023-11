import unittest

from combinations import combinations


class TestCombinations(unittest.TestCase):
    def test_works_for_length_2(self):
        expected = {'aa', 'ab', 'ba', 'bb'}

        actual = combinations({'a', 'b'}, 2)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
