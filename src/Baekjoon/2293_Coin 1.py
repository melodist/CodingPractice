"""
https://www.acmicpc.net/problem/2293
Using dynamic programming
Initial Condition setting
"""
#1. My Solution (340ms)
import sys


input = sys.stdin.readline
n, k = map(int, input().strip().split())
a = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
dp[0] = 1

for i in range(n):
    for j in range(1, k+1):
        if j >= a[i]:
            dp[j] += dp[j - a[i]]
            
print(dp[-1])

#2. Other Solution (168ms)
import sys
In = sys.stdin.readline

n, k = map(int, In().split())
coins = [int(In()) for _ in range(n)]

def foo(coins, k):
    dp = [0] * (k+1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, len(dp)):
            dp[i] += dp[i-coin]
    return dp[-1]

print(foo(coins, k))
