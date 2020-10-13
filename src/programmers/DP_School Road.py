"""
https://programmers.co.kr/learn/courses/30/lessons/42898
Using hash and dynamic programming
"""
#1. My Solution
def solution(m, n, puddles):
    puddles = set([(i, j) for i, j in puddles])
    MOD = 1000000007
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    puddles.add((1, 1))
    for i in range(1, n+1):
        for j in range(1, m+1):
            if (j, i) not in puddles:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[-1][-1] % MOD
    
#2. Other Solution
def solution(m, n, puddles):
    answer = 0
    info = dict([((2, 1), 1), ((1, 2), 1)])
    for puddle in puddles:
        info[tuple(puddle)] = 0

    def func(m, n):
        if m < 1 or n < 1:
            return 0
        if (m, n) in info:
            return info[(m, n)]
        return info.setdefault((m, n), func(m - 1, n) + func(m, n - 1))
    return  func(m, n) % 1000000007
