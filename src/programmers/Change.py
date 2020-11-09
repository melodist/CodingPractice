"""
https://programmers.co.kr/learn/courses/30/lessons/12907?language=python3
Using dynamic programming
"""
#1. My Solution
def solution(n, money):
    MOD = 1000000007
    dp = [0] * (n+1)
    
    dp[0] = 1
    for j in range(1, n+1):
        if j % money[0] == 0:
            dp[j] = 1
        
    for m in money[1:]:
        for j in range(m, n+1):
            dp[j] += dp[j - m] % MOD
            
    return dp[-1]
