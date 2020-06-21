"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/
Using Binary Search
"""
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid) and isBadVersion(mid-1):
                right = mid - 1
            else:
                left = mid + 1
            
