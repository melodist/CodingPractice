"""
https://leetcode.com/problems/edit-distance
Using Dynamic Programming
"""
#1. Solution using memoization (85ms)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = dict()
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == -1: return j + 1
            if j == -1: return i + 1

            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i-1, j-1)
            else:
                memo[(i, j)] = min(
                    dp(i-1, j) + 1,  # delete
                    dp(i, j-1) + 1,  # insert
                    dp(i-1, j-1) + 1 # change
                )

            return memo[(i, j)]

        return dp(len(word1) - 1, len(word2) - 1)

#2. Solution using DP table (184ms)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            dp[i][0] = i

        for j in range(1, n+1):
            dp[0][j] = j

        for j in range(1, n+1):
            for i in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j]+1,
                        dp[i][j-1]+1,
                        dp[i-1][j-1]+1
                    )

        return dp[m][n]
