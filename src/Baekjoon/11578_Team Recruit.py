"""
https://www.acmicpc.net/problem/11578
Using Bit Mask
"""
#1. My Soltuion (68ms)
import sys


input = sys.stdin.readline
n, m = map(int, input().split())
questions = [0] * m
ans = float('inf')

for i in range(m):
    a = list(map(int, input().split()))
    for q in a[1:]:
        questions[i] += 1<<(q-1)
        
for i in range(1, 2**m):
    bit = 0
    for j in range(m):
        if i & 1<<j == 1<<j:
           bit |= questions[j]

    if bit == 2**n - 1:
        ans = min(ans, bin(i).count('1'))

print(ans if ans < float('inf') else -1)
