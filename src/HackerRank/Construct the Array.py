"""
https://www.hackerrank.com/challenges/construct-the-array/problem
Using Dynamic Programming
Cannot make 2D array for DP because of n, k lengths.
"""
def countArray(n, k, x):
    MOD = 10**9+7
    dp0 = dp1 = 0
    dp0old = 1
    for _ in range(2, n+1):
        dp0 = (dp1*(k-1))%MOD
        dp1 = (dp0old + dp1*(k-2))%MOD
        dp0old = dp0
        
    if x==1:
        return dp0
    return dp1
