"""
https://leetcode.com/problems/string-to-integer-atoi/
"""
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
