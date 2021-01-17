"""
https://www.acmicpc.net/problem/9095
Use Dynamic Programming.
reduce, lambda only can use 2 arguments, not over 3.
"""
T = int(input())
for _ in range(T):
    n = int(input())
    dp = [0] * 12

    dp[1:4] = [1, 2, 4]
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
    print(dp[n])
