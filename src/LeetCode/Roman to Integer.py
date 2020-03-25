"""
https://leetcode.com/problems/roman-to-integer/
s번째 문자의 값이 s+1번째 문자의 값보다 작으면 s번째 값은 -가 된다.
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        temp = 0
        
        for i in range(len(s)-1):
            if dic[s[i]] < dic[s[i+1]]:
                temp -= dic[s[i]]
            else:
                temp += dic[s[i]]
            
        return temp + dic[s[-1]]
