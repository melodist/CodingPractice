"""
https://programmers.co.kr/learn/courses/30/lessons/42897?language=python3
Using dynamic programming
Make case for selection of 0
"""
#1. My Solution
def solution(money):
    # dp[i][0] : 0 off / dp[i][1] : 0 on
    dp = [[0] * 2 for _ in range(len(money))]
    dp[0][1] = dp[1][1] = money[0]
    dp[1][0] = money[1]
    for i, m in enumerate(money):
        if 1 < i < len(money) - 1:
            dp[i][0] = max(dp[i-2][0] + m, dp[i-1][0])
            dp[i][1] = max(dp[i-2][1] + m, dp[i-1][1])
        elif i  == len(money) - 1:
            dp[i][0] = max(dp[i-2][0] + m, dp[i-1][0])
            dp[i][1] = dp[i-1][1]

    return max(dp[-1])
    
#2. Other Solution
def solution(a):
    x1, y1, z1 = a[0], a[1], a[0]+a[2]
    x2, y2, z2 = 0, a[1], a[2]
    for i in a[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1)+i
        x2, y2, z2 = y2, z2, max(x2, y2)+i
    return max(x1, y1, y2, z2)
