"""
https://leetcode.com/problems/reverse-integer/
"""
class Solution:
    def reverse(self, x: int) -> int:
        a = abs(x)
        temp = 0
        while a:
            pop = a % 10
            a = a // 10
            
            temp = temp * 10 + pop
            
        if -2 ** 31 <= temp < 2 ** 31:        
            if x >= 0:
                return temp
            else:
                return -temp
        else:
            return 0
