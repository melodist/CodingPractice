"""
https://programmers.co.kr/learn/courses/30/lessons/43105/
Using Dynamic Programming
"""
#1. My Solution
def solution(triangle):
    n = len(triangle)
    dp = [[0] * (n+2) for _ in range(n)]
    dp[0][1] = triangle[0][0]
    for i, row in enumerate(triangle[:-1]):
        for j, x in enumerate(row, 1):
            dp[i+1][j] = max(triangle[i+1][j-1]+dp[i][j], dp[i+1][j])
            dp[i+1][j+1] = max(triangle[i+1][j]+dp[i][j], dp[i+1][j+1])

    return max(dp[-1][1:-1])
    
#2. Other Solution
solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])
