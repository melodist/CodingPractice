"""
https://leetcode.com/contest/weekly-contest-294/problems/percentage-of-letter-in-string/
Weekly Contest 294
String Problem
"""
#1. My Solution (65ms)
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        ans = 0
        for c in s:
            if c == letter: ans +=1
                
        return int(ans / len(s) * 100)
    
#2. Other Solution (50ms)
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return (s.count(letter) * 100) // len(s)
