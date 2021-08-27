"""
https://leetcode.com/problems/sliding-window-maximum/
Using Sliding Window
"""
#1. My Solution (2058ms)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        
        q = deque([])
        for i, n in enumerate(nums):
            while q and nums[q[-1]] < n:
                q.pop()
            q.append(i)
            
            if i >= k-1:
                while q and q[0] < i - k + 1:
                    q.popleft()
                ans.append(nums[q[0]])
                
        return ans
