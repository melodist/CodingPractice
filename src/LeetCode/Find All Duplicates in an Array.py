"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/
Implementation Problem
"""
#1. My Solution
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                answer.append(abs(nums[i]))
            else:
                nums[abs(nums[i]) - 1] *= -1
            
        return answer

#2. Other Solution
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        result = []
        seen = set()
        
        for val in nums:
            if val not in seen:
                seen.add(val)
            else:
                result.append(val)
                
        return result
