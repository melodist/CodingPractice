"""
https://leetcode.com/problems/k-divisible-elements-subarrays/

"""
#1. My Solution
from itertools import combinations


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        def check(subarray):
            cnt_divisible = 0
            for i in subarray:
                if i % p == 0:
                    cnt_divisible += 1
            return True if cnt_divisible <= k else False
        
        n = len(nums)
        answer = set()
        for cnt in range(1, n+1): # elements cnt for subarray
            for i in range(n-cnt+1):
                answer.add(tuple(nums[i:i+cnt])) if check(nums[i:i+cnt]) else 0
                
        return len(answer)
      
#2. Solution using binary search
class Solution:
    def countDistinct(self, nums: List[int], k: int, pref_sum: int) -> int:
        nums2 = [int(x % pref_sum == 0) for x in nums]
        pref_sum = list(accumulate(nums2))
        l = len(pref_sum)
        s = set()
        sol = 0
        for left, x in enumerate(pref_sum):
            if nums2[left] == 1:
                tar = x + k
            else:
                tar = x + 1 + k
            right = bisect_left(pref_sum, tar, lo=left)
            for end in range(left + 1, right + 1):
                t = tuple(nums[left:end])
                if t not in s:
                    s.add(t)
        return len(s)
