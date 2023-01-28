"""
https://leetcode.com/problems/super-egg-drop
Using Dynamic Programming
"""
#1. Solution using binary search (2799ms)
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = dict()

        def dp(k, n):
            # base case
            if n == 0: return 0
            if k == 1: return n

            # memoization
            if (k, n) in memo:
                return memo[(k, n)]

            res = float('inf')

            # throw egg at ith floor
            # for i in range(1, n+1):
            #     res = min(res,
            #         max(
            #             dp(k, n-i), # egg does not break
            #             dp(k-1, i-1) # egg breaks
            #         ) + 1
            #     )

            low, high = 1, n
            while low <= high:
                mid = (low + high) // 2
                broken = dp(k - 1, mid - 1)
                not_broken = dp(k, n - mid)

                if broken > not_broken:
                    high = mid - 1
                    res = min(res, broken + 1)
                else:
                    low = mid + 1
                    res = min(res, not_broken + 1)
            
            memo[(k, n)] = res
            return res
        
        return dp(k, n) # means minimum moves need to determine f with k eggs and n floors
