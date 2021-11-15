"""
https://leetcode.com/problems/largest-divisible-subset/
Using Dynamic Programming
"""
#1. My Solution
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        
        nums.sort()
        
        dp = [(0, 0)] * n
        dp[0] = (1, 0)
        maxIndex, maxVal = 0, 1
        
        for i in range(1, n):
            arr = [(dp[j][0] + 1, j) for j in range(i + 1) if nums[i] % nums[j] == 0]
            dp[i] = max(arr)
            
            if dp[i][0] > maxVal:
                maxIndex, maxVal = i, dp[i][0]
                
        i, lds = maxIndex, [nums[maxIndex]]
        while i != dp[i][1]:
            i = dp[i][1]
            lds.append(nums[i])
        return lds
