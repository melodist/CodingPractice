"""
https://leetcode.com/problems/next-greater-element-i
Using monotonic stack
"""
#1. My Solution (49ms)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = dict()
        s = []
        for i in nums2[::-1]:
            while s and s[-1] <= i:
                s.pop()

            dic[i] = s[-1] if s else -1
            s.append(i)

        return [dic[i] for i in nums1]
