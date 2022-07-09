"""
https://leetcode.com/problems/jump-game-vi/
Using sliding window and dynamic programming
"""
#1. Solution using deque
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        d = deque([(nums[0],0)])
        for i in range(1, len(nums)):
            dp[i] = nums[i] + d[0][0]
            
            while d and d[-1][0] < dp[i]:   # sliding window maximum variation
                d.pop()                     # sliding window maximum variation
            d.append((dp[i],i))             # sliding window maximum variation
            
            if i-k == d[0][1]:              # sliding window maximum variation
                d.popleft()                 # sliding window maximum variation
                
        return dp[-1]
            
#2. Solution using heap
    def maxResult(self, nums: List[int], k: int) -> int:
        highestK = [(-nums[0],0)]
        result = nums[0]  # handles case where there is just 1 itme
        
        for i in range(1,len(nums)):
            while highestK[0][1] < i-k:
                heapq.heappop(highestK)
            result = nums[i] + -highestK[0][0]
            heapq.heappush(highestK, (-result,i))

        return result
