"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
Using two-pointer approach
"""
#1. My Solution (131ms)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n-1

        while left < right:
            twosum = numbers[left] + numbers[right]
            if twosum == target:
                return [left+1, right+1]

            if twosum < target:
                left += 1
            if twosum > target:
                right -= 1

        return [-1, -1]
