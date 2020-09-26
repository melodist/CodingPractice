"""
https://www.acmicpc.net/problem/4307
Using greedy algorithm
"""
#1. My Solution
import sys


for _ in range(int(input())):
    s, n = map(int, sys.stdin.readline().strip().split())
    fast = []
    slow = []
    for _ in range(n):
        x = int(sys.stdin.readline().strip())
        if x < s - x:
            fast.append(x)
            slow.append(s-x)
        else:
            fast.append(s-x)
            slow.append(x)
            
    print(max(fast), max(slow))
