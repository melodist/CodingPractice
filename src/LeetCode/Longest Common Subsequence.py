"""
https://leetcode.com/problems/longest-common-subsequence
Using Dynamic Programming
"""
#1. My Solution (454ms)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        prev = [0] * (m+1)
        curr = [0] * (m+1)

        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    curr[j+1] = prev[j] + 1
                else:
                    curr[j+1] = max(prev[j+1], curr[j])

            prev = curr
            curr = [0] * (m+1)

        return prev[m]
