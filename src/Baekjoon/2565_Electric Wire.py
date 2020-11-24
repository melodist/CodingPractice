"""
https://www.acmicpc.net/problem/2565
Using dynamic programming
Longest Increasing Sequence (LIS) Problem
"""
#1. My Solution (72ms)
import sys


input = sys.stdin.readline
n = int(input())
a = []
for _ in range(n):
    a.append([*map(int, input().split())])
    
a.sort(key=lambda x:x[0])
dp = [0] * n

ans = 0
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if a[j][1] < a[i][1]:  # 기존의 j번째 전깃줄까지 선택한 경우의 값에 i번째 전깃줄을 더할 수 있는 조건
            dp[i] = max(dp[i], dp[j] + 1)
            
    ans = max(ans, dp[i])
    
print(n-ans)

#2. Other Solution (56ms)
from sys import stdin

t = int(stdin.readline())
data = []
D = [0] * t
for _ in range(t):
    data.append(tuple(map(int, stdin.readline().split())))
data.sort()

for i in range(t):
    for j in range(i):
        if data[i][1] > data[j][1]:
            D[i] = max(D[i], D[j] + 1)

print(t - max(D) - 1)
