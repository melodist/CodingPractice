"""
https://leetcode.com/problems/daily-temperatures
Using monotonic stack
"""
#1. My Solution (1349ms)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = []
        for i in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                ans.append(stack[-1] - i)
            else:
                ans.append(0)

            stack.append(i)

        return ans[::-1]
    
    
#2. Other Solution (1335ms)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_idx = stack.pop()
                result[prev_idx] = i - prev_idx
            stack.append(i)
        return result
