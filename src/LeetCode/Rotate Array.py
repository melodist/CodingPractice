"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/646/
"""
#1. Cyclic Replacements
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, count = 0, 0
        while count < n:
            start, cur = i, i
            prev = nums[start]
            while True:
                cur = (cur+k) % n
                next = nums[cur]
                nums[cur] = prev
                prev = next
                count += 1
                if cur == start:
                    break
            i += 1
 
#2. Reverse Lists
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(array, start, end):
            while start < end:
                array[start], array[end] = array[end], array[start]
                start += 1
                end -= 1
                
        n = len(nums)
        k %= n
        
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)
