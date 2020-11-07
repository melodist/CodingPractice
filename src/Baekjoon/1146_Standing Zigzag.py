"""
https://www.acmicpc.net/problem/1146
Using dynamic programming
Store the values for dp(left, right, order)
left: numbers smaller than i
right : numbers bigger than i
order : ascending / descending
"""
#1. My Solution
def problem(n):
    if n == 1:
        return 1
        
    answer = 0
    dp[0][0][0] = 1
    dp[0][0][1] = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                continue
            
            left = j - 2 if i < j else j - 1
            right = n - j if i < j else n - j - 1
            
            order = 1 if i > j else 0
            answer += solve(left, right, order)
            answer %= MOD

    return answer


def solve(left, right, order):
    # order : 0 - ascending / 1 - descending
    if dp[left][right][order] != -1:
        return dp[left][right][order]
    
    temp = 0        
    if order:
        for i in range(1, right+1):
            temp += solve(left+(i-1), right-i, 0)
            temp %= MOD
    else:
        for i in range(1, left+1):
            temp += solve(left-i, right + (i-1), 1)
            temp %= MOD
            
    dp[left][right][order] = temp
    return temp
    
MOD = 1000000
n = int(input())
dp = [[[-1] * 2 for _ in range(n+1)] for _ in range(n+1)]
print(problem(n))
