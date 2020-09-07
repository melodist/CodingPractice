"""
https://www.acmicpc.net/problem/1149
Using Dynamic Programming
"""
#1. Solution using BFS (Memory over / Time over)
import sys
from collections import deque


n = int(input())
arr = [[*map(int, sys.stdin.readline().strip().split())] for _ in range(n)]
answer = float('inf')
q = deque([(0, i, arr[0][i]) for i in range(3)])

while q:
    cur, color, cost = q.popleft()
    if cur == n - 1:
        answer = min(answer, cost)
        continue
    
    for i in range(3):
        if i != color:
            q.append((cur+1, i, cost + arr[cur+1][i]))
            
print(answer)

#2. Solution using DP
import sys


n = int(input())
arr = [[*map(int, sys.stdin.readline().strip().split())] for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0] = arr[0]
d = [(0, 1, 2), (1, 0, 2), (2, 1, 0)]

for i in range(1, n):
    for j, a, b in d:
        dp[i][j] = min(dp[i-1][a], dp[i-1][b]) + arr[i][j]

print(min(dp[-1]))
