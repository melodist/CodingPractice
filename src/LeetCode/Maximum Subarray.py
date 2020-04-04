"""
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3285/
1. Kadane's Algorithm
2. Divide and Conquer
"""
# 1. Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int: 
        best_sum = float('-inf')
        current_sum = 0
        for x in nums:
            if current_sum <= 0:
                current_sum = x
            else:
                # Extend the existing sequence with the current element
                current_sum += x

            if current_sum > best_sum:
                best_sum = current_sum

        return best_sum

# 2. Divide and Conquer
class Solution:
    def maxSubArray(self, nums): 
        return self.maxSubArraySum(nums, 0, len(nums)-1)
    
    def maxSubArraySum(self, nums, left, right): 
        if left == right:
            return nums[left]

        mid = (left + right) // 2

        return max(self.maxSubArraySum(nums, left, mid),
                    self.maxSubArraySum(nums, mid+1, right),
                    self.maxCrossingSum(nums, left, mid, right))
    
    def maxCrossingSum(self, nums, left, mid, right):
        sm = 0; left_sum = float('-inf')
        for i in range(mid, left-1, -1):
            sm += nums[i]

            if sm > left_sum:
                left_sum = sm

        sm = 0; right_sum = float('-inf')
        for i in range(mid+1, right+1):
            sm += nums[i]

            if sm > right_sum:
                right_sum = sm

        return left_sum + right_sum
