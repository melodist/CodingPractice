"""
https://leetcode.com/problems/trapping-rain-water
grid at index[i] can trap water min(l_max, r_max)
"""
#1. Solution using two pointer approach (122ms)
class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = height[0]
        r_max = height[-1]

        left = 0
        right = len(height)-1
        ans = 0

        while left < right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])

            if l_max < r_max:
                ans += l_max - height[left]
                left += 1
            else:
                ans += r_max - height[right]
                right -= 1

        return ans

#2. Solution using memoization (153ms)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max = [0] * n
        r_max = [0] * n
        l_max[0] = height[0]
        r_max[-1] = height[-1]

        for i in range(1, n):
            l_max[i] = max(l_max[i-1], height[i])

        for i in range(n-2, -1, -1):
            r_max[i] = max(r_max[i+1], height[i])

        ans = 0
        for i in range(n):
            ans += min(l_max[i], r_max[i]) - height[i]

        return ans
