"""
https://www.hackerrank.com/challenges/two-characters/problem
Brute Force problem
"""
#1. My Solution
from itertools import permutations


def validate(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
        
    return True


def alternate(s):
    ind = set()
    for c in s:
        ind.add(c)
    
    ans = 0
    for a, b in permutations(ind, 2):
        chk = [c for c in s if c==a or c==b]
        if validate(chk):
            ans = max(ans, len(chk))

    return ans
