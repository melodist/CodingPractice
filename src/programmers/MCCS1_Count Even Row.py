"""
https://programmers.co.kr/learn/courses/30/lessons/68647/
Using dynamic programming and combinatorics
"""
#1. My Solution
from math import comb


def solution(a):
    n = len(a); m = len(a[0])
    dp = [[0] * (n+1) for _ in range(m+1)]
    dp[0][n] = 1  # 0 is even, all row in col 0 has even elements
    cols = [r.count(1) for r in zip(*a)]
    combs = {}

    for c in range(1, m+1):
        for r in range(n+1):
            for r2 in range(n+1):
                a1, b1 = n-r2, r2  # a1 means 1 of prev column, b1 means 0 of prev column
                a2, b2 = cols[c-1], n-cols[c-1]  # a2 means 1 of current column, b1 means 0 of current column
                x2 = (r + a2 - b1)
                if x2 % 2:
                    continue
                x = x2 // 2
                y = r - x
                if 0 <= x <= a2 and 0 <= y <= b2:
                    if (a1, x) not in combs:
                        combs[(a1, x)] = comb(a1, x)
                    if (b1, y) not in combs:
                        combs[(b1, y)] = comb(b1, y)

                    i = combs[(a1, x)]
                    j = combs[(b1, y)]
                    dp[c][r] += (dp[c-1][r2] * i * j)
            dp[c][r] %= 10**7 + 19

    return dp[m][n]
