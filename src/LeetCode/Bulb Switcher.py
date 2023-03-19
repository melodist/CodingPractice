"""
https://leetcode.com/problems/bulb-switcher
Only bulb at index a which meets a = b^2 will turn on
"""
#1. My Solution (25ms)
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**0.5)
    
#2. Other Solution (19ms)
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return isqrt(n)
