"""
https://www.hackerrank.com/challenges/number-list
Mathematical Problem
"""
#1. My Solution
from itertools import groupby

def solve(a, k):
    segs = [len(list(j)) for i,j in groupby(a, lambda x:x>k) if not i]
    return math.comb(len(a)+1,2) - sum(math.comb(i+1,2) for i in segs)
