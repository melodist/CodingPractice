"""
https://leetcode.com/problems/binary-search
Using Binary Search
"""
#1. Solution using while loop ()
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + int((right - left + 1) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return -1
      
#2. Solution using recursion
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def rec(start, end):
            if start <= end:
                mid = (start+end) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return rec(mid+1, end)
                elif nums[mid] > target:
                    return rec(start, mid-1)
            else:
                return -1
        return rec(0, len(nums)-1)
