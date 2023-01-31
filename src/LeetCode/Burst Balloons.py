"""
https://leetcode.com/problems/burst-balloons
Using Dynamic Programming
"""
#1. My Solution (5814ms)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        points = [1] + nums + [1]

        # dp[i][j] means best score when burst balloons between index i and j
        dp = [[0] * (n+2) for _ in range(n+2)]

        # To find dp[i][j], i should go downward, and j should go right
        # k means index that last balloon be bursted
        for i in range(n, -1, -1):
            for j in range(i+1, n+2):
                for k in range(i+1, j):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + points[i] * points[k] * points[j])

        return dp[0][n+1]
