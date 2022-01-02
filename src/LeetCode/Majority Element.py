"""
https://leetcode.com/problems/majority-element/
Using Boyer-Moore Voting Algorithm
"""
#1. My Solution (175ms)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        ans = nums[0]
        for i in nums[1:]:
            if count == 0:
                count += 1
                ans = i
            elif ans == i:
                count += 1
            else:
                count -= 1
                
        return ans
    
#2. Other Solution (156ms)
import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)//2
        return nums[n]
