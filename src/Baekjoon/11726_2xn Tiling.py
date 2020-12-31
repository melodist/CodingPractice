"""
https://www.acmicpc.net/problem/11726
Using dynamic programming
"""
#1. My Solution (72ms)
n = int(input())
mod = 10007

dp = [0, 1, 2] + [0] * 998
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % mod
    
print(dp[n])

#2. Other Solution (56ms)
n=int(input())
a,b=1,1
for i in range(n):a,b=b,a+b
print(a%10007) 
