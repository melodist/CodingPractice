"""
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3283/
A ^ A = 0, A ^ B = B ^ A
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = nums[0]
        for i in range(1, len(nums)):
            answer ^= nums[i]
        return answer
