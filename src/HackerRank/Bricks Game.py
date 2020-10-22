"""
https://www.hackerrank.com/challenges/play-game/problem
Using dynamic programming
"""
#1. Solution
def bricksGame(a):
    n=len(a)
    dp=[0]*(n+4)
    s=0
    for i in range(n-1,-1,-1):
        s+=a[i]
        dp[i]=s-(min(dp[i+1],dp[i+2],dp[i+3]))
    return dp[0]
