"""
https://leetcode.com/problems/string-to-integer-atoi/
"""
#1. My Solution
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()
        if not str: return 0
        
        if str[0] == '-':
            flag = False
            ans = 0
        elif str[0] == '+':
            flag = True
            ans = 0
        elif not str[0].isdigit():
            return 0
        else:
            flag = True
            ans = int(str[0])
        
        for char in str[1:]:
            if char.isdigit():
                ans = 10 * ans + int(char)
            else:
                break
                
        ans = ans if flag else -ans
            
        return min(2**31-1, max(-2**31, ans))

#2. Solution Using Regex
import re


class Solution:
    def myAtoi(self, str: str) -> int:
        re_match = re.search('^(\s)*(\t)*[-+]{0,1}[0-9]+', str)
        if re_match is None:
            return 0
        else:
            num = int(str[re_match.start():re_match.end()])
            if num <= -2 ** 31: 
                return -2 ** 31
            elif num > 2**31 -1:
                return 2**31 -1
            return num
