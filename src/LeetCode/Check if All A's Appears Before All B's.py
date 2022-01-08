"""
https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
Implementation Problem
"""
#1. My Solution (46ms)
class Solution:
    def checkString(self, s: str) -> bool:
        n_a = n_b = 0
        for c in s:
            if c == 'a':
                if n_b > 0:
                    return False
                else:
                    n_a += 1
            else:
                n_b += 1
        return True
        
#2. Other Solution (20ms)
class Solution:
    def checkString(self, s: str) -> bool:
        seen_b = False
        for char in s:
            if char == 'b':
                seen_b = True
                
            if char == 'a' and seen_b:
                return False
            
        return True
