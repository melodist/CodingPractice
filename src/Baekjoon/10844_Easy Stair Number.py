"""
https://www.acmicpc.net/problem/10844
Using dynamic programming
"""
#1. My Solution (72ms)
import sys


input = sys.stdin.readline
MOD = 10**9
n = int(input())
dp = [[0] * (10) for _ in range(n+1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    dp[i][0] = dp[i-1][1]
    for j in range(1, 9):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MOD
    dp[i][9] = dp[i-1][8]
    
print(sum(dp[-1]) % MOD)

#2. Other Solution (52ms)
n = int(input())

DP = [[0]*10 for i in range(101)]
DP[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            DP[i][j] = DP[i-1][j+1]
        elif j == 9:
            DP[i][j] = DP[i-1][j-1]
        else:
            DP[i][j] = DP[i-1][j+1] + DP[i-1][j-1]
result = 0
for i in range(0,10):
    result += DP[n][i]

print(result%1000000000)
