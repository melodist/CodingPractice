"""
https://www.acmicpc.net/problem/9375
Implementation Problem
"""
#1. My Solution (120ms)
from collections import Counter
from functools import reduce


for _ in range(int(input())):
    n = int(input())
    wear = []
    for _ in range(n):
        a, b = input().split()
        wear.append(b)

    print(reduce(lambda x, y: x*(y+1), Counter(wear).values(), 1) - 1)
