"""
https://leetcode.com/problems/target-sum
Using Dynamic Programming

While A and B is subset of nums,
sum(A) - sum(B) = target
sum(A) = target + sum(B)
sum(A) + sum(A) = target + sum(B) + sum(A)
2 * sum(A) = target + sum(nums)
sum(A) = (target + sum(nums)) / 2

Transform the problem to find number of subset has sum = (target + sum(nums)) / 2
"""
#1. My Solution (158ms)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def subsets(nums, target):
            n = len(nums)
            dp = [[0] * (target + 1) for _ in range(n+1)]

            print(dp, target)
            # base case
            for i in range(n+1):
                dp[i][0] = 1

            for i in range(1, n+1):
                for j in range(target+1):
                    if (j >= nums[i-1]):
                        dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                    else:
                        dp[i][j] = dp[i-1][j]
            
            return dp[n][target]

        sum_nums= sum(nums)
        if sum_nums < target or (sum_nums + target) % 2 == 1 or sum_nums + target < 0:
            return 0
        
        return subsets(nums, int((sum_nums + target) / 2))
