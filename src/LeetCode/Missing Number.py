"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/
"""
#1. My Solution - Gauss' Formula
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n+1) // 2 - sum(nums)

#2. Bit Manipulation
# [0, 4, 1, 2]
# 4 ^ (0^0) ^ (1^4) ^ (2^1) ^ (3^2)
# = (0^0) ^ (1^1) ^ (2^2) ^ (4^4) ^ 3 = 3
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i, x in enumerate(nums):
            result ^= i ^ x
            
        return result
