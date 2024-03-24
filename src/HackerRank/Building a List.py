"""
https://www.hackerrank.com/challenges/building-a-list
Mathematical Problem
"""
#1. My Solution
def solve(s):
    return sorted(''.join(x) for r in range(1,1+len(s)) for x in combinations(s,r))
