"""
https://www.acmicpc.net/problem/17404
Using Dynamic Programming
Store the cases for each first color
"""
#1. My Solution (88ms)
import sys


input = sys.stdin.readline
n = int(input())
dp = [[[float('inf')] * 3 for _ in range(3)] for _ in range(n)]
cost = [*map(int, input().split())]
for j in range(3):
    for k in range(3):
        if j == k:
            dp[0][j][k] = cost[j]
  
for i in range(1, n):
    cost = [*map(int, input().split())]
    for j in range(3):
        for k in range(3):
            dp[i][j][k] = min(dp[i-1][j][k-1], dp[i-1][j][(k+1) % 3]) + cost[k]
    
for j in range(3):
    dp[-1][j][j] = float('inf')
    
print(min([min(r) for r in dp[-1]])) # not min(min(dp[-1]))
