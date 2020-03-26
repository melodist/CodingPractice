"""
https://leetcode.com/problems/sort-colors/
1. Counting Sort: Two-pass Algorithm
2. One-pass Algorithm using two-point approach
"""
class Solution:
    def sortColors_countingsort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0 for x in range(3)]
        for num in nums:
            count[num] += 1
        
        for i in range(len(nums)):
            if i < count[0]:
                nums[i] = 0
            elif i < count[0] + count[1]:
                nums[i] = 1
            else:
                nums[i] = 2

    def sortColors_onepass(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ren = [1] * n
        zeropoint = 0
        twopoint = n-1
        
        for i in range(n):
            if nums[i] == 0:
                ren[zeropoint] = 0
                zeropoint += 1
            elif nums[i] == 2:
                ren[twopoint] = 2
                twopoint -= 1
                
        nums[:] = ren[:]
