"""
https://leetcode.com/problems/3sum/
Using Two-Pointer Approach
"""
#1. My Solution (1028ms)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            j, k = i+1, N-1
            while j<k:
                if nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
                    
        return result

#2. Other Solution (1201ms)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSumTarget(nums, start, target):
            lo = start
            hi = len(nums) - 1
            res = []
            while lo < hi:
                left = nums[lo]
                right = nums[hi]
                sum_ = left + right
                if sum_ < target: lo += 1
                elif sum_ > target: hi -= 1
                else:
                    res.append([left, right])
                    while lo < hi and nums[lo] == left: lo += 1
                    while lo < hi and nums[hi] == right: hi -= 1

            return res

        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            subsets = twoSumTarget(nums, i+1, -nums[i])
            for s in subsets:
                res.append(s + [nums[i]])


        return res
