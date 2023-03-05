"""
https://leetcode.com/problems/koko-eating-bananas
Using binary search
"""
#1. My Solution (591ms)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculcateSpeed(piles, speed):
            hours = 0
            for k in piles:
                q, r = divmod(k, speed)
                hours += q if r == 0 else q + 1
            return hours

        left = 1
        right = max(piles)

        while left <= right:
            mid = int((left + right) / 2)

            if calculcateSpeed(piles, mid) <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left

#2. Other Solution (372ms)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinishEating(k):
            res=0
            for p in piles:
                res += ceil(p/k)
            return res <= h
        
        l, r = 1, max(piles)
        while l <= r:
            mid = (l+r)//2
            if canFinishEating(mid):
                r = mid-1
            else:
                l = mid+1
        return l
