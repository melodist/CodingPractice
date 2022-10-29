"""
https://leetcode.com/problems/coin-change
Using Dynamic Programming
"""
#1. My Solution (6035ms)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()
        def dp(n):
            if n in memo: return memo[n]
            
            # base case
            if n == 0: return 0
            if n < 0: return -1

            res = float('inf')
            for coin in coins:
                subproblem = dp(n-coin)
                if subproblem != -1:
                    res = min(res, subproblem + 1)

            memo[n] = res if res != float('inf') else -1
            return memo[n]

        return dp(amount)
