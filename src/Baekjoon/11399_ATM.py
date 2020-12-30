"""
https://www.acmicpc.net/problem/11399
Implementation Problem
"""
#1. My Solution (68ms)
import sys


input = sys.stdin.readline
n = int(input())
p = [*map(int, input().split())]
p.sort(reverse=True)
ans = 0
for i, p in enumerate(p, 1):
    ans += i * p

print(ans)
