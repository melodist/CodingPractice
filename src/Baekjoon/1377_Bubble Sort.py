"""
https://www.acmicpc.net/problem/1377
Using Sort
Calculate maximum shifts to left
"""
#1. My Solution (256ms)
import sys


input = sys.stdin.readline
n = int(input())
a = []
ind = [0] * 100_000_1
for i in range(n):
    a.append((int(input()), i))
    
sorted_a = sorted(a)
cnt = 0

# Find move left
for i, p in enumerate(sorted_a):    
    cnt = max(cnt, p[1] - i)
    
print(cnt+1)
