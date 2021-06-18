"""
https://www.acmicpc.net/problem/2011
Using Dynamic Programming
"""
#1. My Solution (72ms)
s = input()
mod = 1_000_000

n = len(s)
s = '0' + s
dp = [0] * (n+1)
dp[0] = 1

for i in range(1, n+1):
    if s[i] != '0' :
        dp[i] += dp[i-1] % mod
    if 9 < int(s[i-1:i+1]) < 27:
        dp[i] += dp[i-2] % mod

print(dp[-1] % mod)
