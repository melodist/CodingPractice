"""
https://www.hackerrank.com/challenges/x-and-his-shots/problem
Using Binary Search and Sort
Sort players range and find index of each shot
"""
#1. My Solution
from bisect import bisect_left, bisect_right


def solve(shots, players):
    a, b = list(zip(*shots))
    c, d = map(list, list(zip(*players)))
    c.sort()
    d.sort()

    return sum(bisect_right(c,v) for v in b) - sum(bisect_left(d,u) for u in a)
