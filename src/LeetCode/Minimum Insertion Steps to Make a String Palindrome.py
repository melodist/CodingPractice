"""
https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome
Using Dynamic Programming
"""
#1. My Solution (639ms)
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n-2, -1, -1):
            for j in range(i, n):
                dp[i][j] = dp[i+1][j-1] if s[i] == s[j] else min(dp[i][j-1], dp[i+1][j]) + 1

        return dp[0][n-1]
