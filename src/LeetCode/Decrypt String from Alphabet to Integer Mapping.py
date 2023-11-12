"""
https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping
String Problem
"""
#1. My Solution (38ms)
class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ''
        p = len(s) - 1

        while p >= 0:
            c = s[p]

            if c == '#':
                ans += chr(96 + int(s[p-2:p]))
                p -= 2
            else:
                ans += chr(96 + int(c))
                
            p -=1
        
        return ans[::-1]
