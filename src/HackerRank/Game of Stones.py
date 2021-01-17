"""
https://www.hackerrank.com/challenges/game-of-stones-1/problem
Game theory problem
"""
#1. Solution using pattern
def gameOfStones(n):
    return ["First","Second"][n%7 in [0,1]]

#2. Solution using dynamic programming
def gameOfStones(n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(6, n+1):
        dp[i] = 0 if dp[i-2] == 1 or dp[i-3] == 1 or dp[i-5] == 1 else 1
    
    return 'First' if dp[n] == 0 else 'Second'
