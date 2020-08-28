"""
https://www.hackerrank.com/challenges/sherlock-and-cost/problem
Using Memoization
Note that there are only 2 cases for choosing A[i] value.
1. Choosing 1
2. Choosing B[i]
"""
#1. My Solution - Timeout in python 3. Accpeted in Pypy 3
def cost(B):
    n = len(B)
    dp = [[0] * 101 for _ in range(n)]

    for i in range(1, n):
        for j in (1, B[i-1]):
            dp[i][1] = max(dp[i][1], dp[i-1][j] + abs(j - 1))
            dp[i][B[i]] = max(dp[i][B[i]], dp[i-1][j] + abs(j - B[i]))

    return max(dp[-1])

#2. Optimal Solution
def cost(B):
    n = len(B)
    hi, low= 0, 0
    for i in range(1, n):
        high_to_low_diff = abs(B[i-1] - 1)
        low_to_high_diff = abs(B[i] - 1)
        high_to_high_diff = abs(B[i] - B[i-1])
        
        low_next = max(low, hi+high_to_low_diff)
        hi_next = max(hi+high_to_high_diff, low+low_to_high_diff)
        
        low = low_next
        hi = hi_next
    
    return max(hi,low)
