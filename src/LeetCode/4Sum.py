"""
https://leetcode.com/problems/4sum
Using two-pointer approach
"""
#1. My Solution (921ms)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def threeSum(nums, start, target):
            res = []
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                subsets = twoSum(nums, i+1, target - nums[i])
                for s in subsets:
                    res.append([nums[i]] + s)

            return res

        def twoSum(nums, start, target):
            res = []
            lo = start
            hi = len(nums) - 1

            while lo < hi:
                left = nums[lo]
                right = nums[hi]

                if left + right == target:
                    res.append([left, right])
                    while lo < hi and left == nums[lo]: lo += 1
                    while lo < hi and right == nums[hi]: hi -= 1

                if left + right < target:
                    lo += 1

                if left + right > target:
                    hi -= 1

            return res

        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            subsets = threeSum(nums, i+1, target - nums[i])
            for s in subsets:
                res.append([nums[i]] + s)

        return res
    
#2. Other Solution (78ms)
class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         # all_possible = list()
#         # for i in range(len(nums)+1):
#         #     all_possible+=list(itertools.combinations(nums, i))

#         all_possible = list(itertools.combinations(nums, 4))
        
#         all_possible_length_four = [sorted(list(x)) for x in all_possible]
#         #removing duplicates
#         fresh = list()
#         [fresh.append(x) for x in all_possible_length_four if x not in fresh]
#         final_result = [final_list for final_list in fresh if sum(final_list)==target]
#         return final_result

    def fourSum(self, nums, target):
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                l,r = 0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results
