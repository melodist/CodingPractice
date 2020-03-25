"""
https://leetcode.com/problems/3sum/
Two-Pointer Approach
"""
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
