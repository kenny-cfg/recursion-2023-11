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
from typing import Set


def combinations(characters: Set[str], length: int) -> Set[str]:
    if length == 0:
        return {''}
    smaller_combinations = combinations(characters, length - 1)
    return {
        character + combination
        for character in characters
        for combination in smaller_combinations
    }


if __name__ == '__main__':
    result = combinations({'a', 'b', 'c'}, 5)
    print(result)
