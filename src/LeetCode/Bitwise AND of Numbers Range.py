"""
https://leetcode.com/problems/bitwise-and-of-numbers-range/
Bitwise Problem
"""
#1. My Solution
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        counter = 0
        while(left!=right):
            left = left>>1
            right =right>>1
            counter+=1
        return left<<counter
