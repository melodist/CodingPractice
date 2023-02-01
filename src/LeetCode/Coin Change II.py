"""
https://leetcode.com/problems/coin-change-ii
Using Dynamic Programming
"""
#1. My Solution (315ms)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # dp[n][amount] means number of combinations for coins[:n+1] which make up amount
        prev = [1] + [0] * amount
        curr = [1] + [0] * amount

        for i in range(1, n+1):
            for j in range(1, amount+1):
                if j >= coins[i-1]:
                    curr[j] = prev[j] + curr[j - coins[i-1]]
                else:
                    curr[j] = prev[j]

            prev = curr

        return prev[amount]
