"""
https://www.hackerrank.com/challenges/game-of-throne-ii
Combinatorics Problem
"""
#1. My Solution
from collections import Counter


def solve(s):
    num=int(len(s)/2)

    ca=math.factorial(num)

    cou=Counter(s)

    for i in cou:
        ca=ca//math.factorial(int(cou[i]/2))

    return (ca%((10**9)+7))
