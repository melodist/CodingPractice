"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/
"""
#1. My Solution
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return format(x ^ y, 'b').count('1')

#2. Without using casting
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        ans = 0
        while xor:
            ans += xor & 1
            xor >>= 1
            
        return ans
