"""
https://leetcode.com/problems/subsets
"""
#1. Solution using recursion (38ms)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        n = nums.pop()
        
        res = self.subsets(nums)
        for i in range(len(res)):
            res.append(res[i] + [n])

        return res

#2. Solution using backtracking (32ms)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums):
            if not nums: return [[]]
            n = nums.pop()
            
            res = backtrack(nums)
            for i in range(len(res)):
                res.append(res[i] + [n])

            return res

        return backtrack(nums)
