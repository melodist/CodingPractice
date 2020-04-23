"""
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3307/
1. hashmap 이용. prevsum = cursum - k를 만족하는 prevsum의 갯수만큼 답에 더한다.
Time complexity O(n) / Space complexity O(n)
2. 2-point approach. Time complexity O(n^2) / Space complexity O(1)
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans, cursum = 0, 0
        prevSum = defaultdict(lambda: 0)

        for i in range(n):
            cursum += nums[i]

            if cursum == k:
                ans += 1

            # prevsum = cursum - k -> k = cursum - prevsum
            if (cursum - k) in prevSum:
                ans += prevSum[cursum - k]

            prevSum[cursum] += 1
                    
        return ans
        
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            sum = 0

            for j in range(i, n):
                sum += nums[j]
                if sum == k:
                    ans += 1
        return ans
