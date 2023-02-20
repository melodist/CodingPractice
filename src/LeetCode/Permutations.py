"""
https://leetcode.com/problems/permutations
Using backtracking
"""
#1. My Solution (57ms)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, track):
            if len(track) == len(nums):
                res.append(track[::])
                return

            for i in range(len(nums)):
                if nums[i] in set(track):
                    continue
                track.append(nums[i])
                backtrack(nums, track)
                track.pop()

        res = []
        track = []
        backtrack(nums, track)
        return res

#2. Other Solution (32ms)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            for j in self.permute(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + j)
        return res
