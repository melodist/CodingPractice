"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
Implementation Problem
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] != 0:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
