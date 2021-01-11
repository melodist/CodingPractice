"""
https://www.acmicpc.net/problem/18870
Using hash and sort
"""
#1. My Solution (1752ms)
import sys


input = sys.stdin.readline
n = int(input())
a = [*map(int, input().split())]
b = sorted([*set(a)])
c = {x:i for i, x in enumerate(b)}
print(' '.join(map(str, [c[x] for x in a])))
