"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/
"""
#1. My Solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        else:
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = nums[1]
            dp[2] = dp[0] + nums[2]

            for i in range(3, len(nums)):
                dp[i] = nums[i] + max(dp[i-3], dp[i-2])

            return max(dp[n-1], dp[n-2])
            
#2. Optimal Solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        max_money = [0] * len(nums)
        max_money[0], max_money[1] = nums[0], max(nums[0], nums[1])
        for idx in range(2, len(nums)):
            max_money[idx] = max(max_money[idx - 2] + nums[idx],
                                max_money[idx - 1])
        return max_money[-1]
