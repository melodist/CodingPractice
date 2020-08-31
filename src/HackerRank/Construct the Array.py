"""
https://www.hackerrank.com/challenges/construct-the-array/problem
Using Dynamic Programming
Cannot make 2D array for DP because of n, k lengths.
If dp[i][j] is the number of ways to make the array of length i ends with j
dp[1][1] = 1, dp[1][2] ... dp[1][k] = 0
dp[i][j] = sum(dp[i-1]) - dp[i-1][j]
dp[i][2] = dp[i][3] ... dp[i][k] for all i and k
"""
def countArray(n, k, x):
    MOD = 10**9+7
    dp0 = dp1 = 0
    dp0old = 1
    for _ in range(2, n+1):
        # dp[i][1] = dp[i-1][x] * (k-1), since dp[i-1][2] = dp[i-1][3] = ... = dp[i][k]
        dp0 = (dp1*(k-1))%MOD
        # dp[i][x] = dp[i-1][1] + dp[i-1][x] * (k-2)
        # for calculte dp[i][x], we exclude 1 and x
        dp1 = (dp0old + dp1*(k-2))%MOD
        dp0old = dp0
        
    if x==1:
        return dp0
    return dp1
