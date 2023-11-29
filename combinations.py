"""
Return all possible combinations of strings of given length,
which can be formed from a set of supplied characters.

Input:
char_set = {'a', 'b'}, length = 3

Output:
aaa
aab
aba
abb
baa
bab
bba
bbb

NB: we cannot use itertools product or permutations functions.
"""


def combinations(characters, length: int):
    if length == 0:
        return {''}
    smaller_combinations = combinations(characters, length - 1)
    return {
        character + combination
        for character in characters
        for combination in smaller_combinations
    }
