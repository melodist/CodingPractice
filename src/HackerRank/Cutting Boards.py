"""
https://www.hackerrank.com/challenges/board-cutting/problem
Using greedy algorithm
To minimize the cost, sort the cost in descending order and use the higher cost first.
"""
#1. My Solution
def boardCutting(cost_y, cost_x):
    cost_x.sort(reverse=True)
    cost_y.sort(reverse=True)
    
    n, m = len(cost_x), len(cost_y)
    i, j = 0, 0
    ans = 0
    MOD = 10**9 + 7
    while i < n or j < m:
        if j < m and i < n:
            if cost_x[i] < cost_y[j]:
                ans += cost_y[j] * (i+1)
                j += 1
            else:
                ans += cost_x[i] * (j+1)
                i += 1
        elif i < n:
            ans += cost_x[i] * (j+1)
            i += 1
        else:
            ans += cost_y[j] * (i+1)
            j += 1
    
    return ans % MOD
