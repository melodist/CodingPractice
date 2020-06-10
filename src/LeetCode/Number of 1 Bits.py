"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/565/
Bit Manipulation Trick
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n != 0:
            ans += 1
            n = n&(n-1)
        return ans
