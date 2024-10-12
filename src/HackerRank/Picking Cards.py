"""
https://www.hackerrank.com/challenges/picking-cards
Combinatorics Problem
"""
#1. My Solution
from itertools import accumulate

def solve(c):
    cnt, mod = [0] * max(len(c), max(c)+1), 1000000007
    for i in c:
        cnt[i]+=1
    return math.prod(x-i for i, x in enumerate(accumulate(cnt))) % mod
        
