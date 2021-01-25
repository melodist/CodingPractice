"""
https://www.hackerrank.com/challenges/nim-game-1/problem
https://math.stackexchange.com/questions/416042/why-does-the-xor-operator-work
"""
#1. My Solution
from functools import reduce


def nimGame(pile):
    return 'First' if reduce(lambda x, y : x^y, pile) != 0 else 'Second'
