"""
https://leetcode.com/problems/longest-palindromic-subsequence
Using Dynamic Programming
"""
#1. My Solution (974ms)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [1] * n # dp[i]

        for i in range(n-2, -1, -1):
            pre = 0
            for j in range(i+1, n):
                temp = dp[j]

                if s[i] == s[j]:
                    dp[j] = pre + 2
                else:
                    dp[j] = max(dp[j], dp[j-1])
                pre = temp

        return dp[n-1]
