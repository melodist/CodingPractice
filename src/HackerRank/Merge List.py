"""
https://www.hackerrank.com/challenges/merge-list
Mathematical Problem

Merging two lists having sizes N and M
is equivalent to arranging M objects of one kind and N objects of another kind in a row
"""
#1. My Solution
def solve(n, m):
    return math.comb(n+m, m) % (10**9 + 7)

