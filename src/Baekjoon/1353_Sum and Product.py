"""
https://www.acmicpc.net/problem/1353
Using mathematics
Arithmetic Mean-Geometric Mean inequality
"""
#1. My Solution
import math

s, p = map(int, input().split())
def solve(s, p):
    if s == p:
        return 1
        
    prev = 0
    x = 2
    while True:
        cur = (s / x) ** x
        if cur >= p:
            return x
        elif cur < prev:
            return -1
        
        prev = cur
        x += 1
        
print(solve(s, p))
