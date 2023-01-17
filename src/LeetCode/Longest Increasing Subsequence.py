"""
https://leetcode.com/problems/longest-increasing-subsequence
Using Dynamic Programming
"""
#1. Solution using DP (3877ms)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] means length of LIS for nums[:i+1]
        n = len(nums)
        dp = [1] * n
    
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
      
#2. Solution using binary search (95ms)
"""
patience sorting
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        top = []

        for n in nums:
            # Find left edge
            left = 0
            right = len(top)

            while left < right:
                mid = int((left + right) / 2)
                if top[mid] > n:
                    right = mid
                elif top[mid] < n:
                    left = mid + 1
                else:
                    right = mid

            # Make new pile
            if left == len(top):
                top.append(n)
            else:
                top[left] = n
                
        return len(top)
