"""
https://www.hackerrank.com/challenges/k-candy-store
Mathematical Problem
"""
#1. My Solution
def solve(n, k):
    return math.comb(n + k - 1, k) % 10 ** 9
