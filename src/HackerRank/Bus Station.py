"""
https://www.hackerrank.com/challenges/bus-station
Mathematical Problem
"""
#1. My Solution
def solve(a):
    sl = sum(a)
    acum = list(itertools.accumulate(a))
    aset = set(acum)
    return [a for a in acum if sl % a == 0 and all(b in aset for b in range(a, sl, a))]
