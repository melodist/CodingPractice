"""
https://leetcode.com/problems/house-robber-ii
Using Dynamic Programming
"""
#1. My Solution (30ms)
class Solution:
    def rob(self, nums: List[int]) -> int:
        # case 1. not rob first and last
        # case 2. rob first
        # case 3. rob last
        # exclude case 1

        if len(nums) == 1: return nums[0]

        # rob last
        curr = next_1 = next_2 = 0
        for i in nums[-1:0:-1]:
            curr = max(next_2 + i, next_1)
            next_2 = next_1
            next_1 = curr
            
        rob_last = next_1

         # rob first
        curr = next_1 = next_2 = 0
        for i in nums[-2::-1]:
            curr = max(next_2 + i, next_1)
            next_2 = next_1
            next_1 = curr       

        return max(rob_last, next_1)
