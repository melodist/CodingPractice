"""
https://www.acmicpc.net/problem/2193
Using dynamic programming
"""
#1. My Solution (72ms)
n = int(input())

dp = [0] * (n+1)
dp[1] = 1
for i in range(2, n+1):
    for j in range(i-1):
        dp[i] += dp[j]
    dp[i] += 1

print(dp[n])

#2. Other Solution (52ms)
a,b=1,1
for i in range(int(input())-2):a,b=b,a+b
print(b)
