"""
https://www.acmicpc.net/problem/15666
Using recursion
"""
#1. My Solution (72ms)
import sys

def solve(i, m, a, b):
    n = len(a)
    if len(b) == m:
        print(' '.join(map(str, b)))
        return
    
    for j in range(i, n):
        solve(j, m, a, b + [a[j]])
        
        
input = sys.stdin.readline
n, m = map(int, input().split())
a = sorted([*set(map(int, input().split()))])
    
solve(0, m, a, [])

#2. Other Solution (56ms)
from itertools import combinations_with_replacement

n, m = map(int, input().split())
arr = sorted(set(input().split()), key=lambda x: int(x))

print("\n".join(map(" ".join, combinations_with_replacement(arr, m))))
