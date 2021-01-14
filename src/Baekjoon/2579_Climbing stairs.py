"""
https://www.acmicpc.net/problem/2579
Using dynamic programming
"""
#1. My Solution (68ms)
import sys


input = sys.stdin.readline
a = []
n = int(input())
for _ in range(n):
    a.append(int(input()))

def solve():
    dp = [0] * n
    if n == 1:
        return a[0]
    if n == 2:
        return a[0]+a[1]

    dp[0] = a[0]
    dp[1] = max(a[0]+a[1], a[1])
    dp[2] = max(a[0]+a[2], a[1]+a[2])
    for i in range(3, n):
        dp[i] = max(a[i] + dp[i-2], a[i] + a[i-1] + dp[i-3])
        
    return dp[n-1]
    
print(solve())
