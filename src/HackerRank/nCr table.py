"""
https://www.hackerrank.com/challenges/ncr-table/problem
Mathematical Problem
"""
#1. My Solution
def solve(n):
    ncr = []
    for r in range (n//2 + 1):
        ncr.append(math.comb(n, r)%(10**9))
    if n % 2== 0:
        return ncr + ncr[:-1][::-1]
    else:
        return ncr + ncr[::-1]
