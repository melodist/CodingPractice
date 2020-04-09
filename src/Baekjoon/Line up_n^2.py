"""
https://www.acmicpc.net/problem/2631
Longest Common Subsequence problem between orginal and sorted array
Using Dynamic Programming
"""
n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
    
dp = [[0 for i in range(n+1)] for j in range(n+1)]
sort_a = sorted(a)

for i in range(n+1):
    for j in range(n+1):
        # dp[i][j] means LIS value from i to j
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif a[i-1] == sort_a[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
print(n - dp[n][n])
