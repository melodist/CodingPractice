"""
https://www.acmicpc.net/problem/15657
"""
#1. My Solution
import sys


def solve(a, i):
    if len(a) == m:
        print(' '.join(map(str, a)))
        return
    
    for j, u in enumerate(arr[i:], i):
        solve(a + [u], j)


input = sys.stdin.readline

n, m = map(int, input().split())
arr = [*map(int, input().split())]
arr.sort()

solve([], 0)

#2. Other Solution
from itertools import combinations_with_replacement

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))

print("\n".join(map(" ".join, combinations_with_replacement(map(str, arr), m))))
