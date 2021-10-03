"""
https://leetcode.com/problems/jump-game/submissions/
Implementation Problem
"""
#1. My Solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_right = nums[0]
        for i in range(len(nums)):
            if cur_right < i:
                return False
            else:
                cur_right = max(cur_right, nums[i]+i)
        return True
