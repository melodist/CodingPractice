"""
https://leetcode.com/contest/weekly-contest-272/problems/find-first-palindromic-string-in-the-array/
Implementation Problem
"""
#1. My Solution (56ms)
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(w):
            n = len(w)
            for i in range(n // 2):
                if w[i] != w[n-1-i]:
                    return False
            return True
        
        for w in words:    
            if isPalindrome(w):
                return w
        return ""
    
#2. Other Solution (44ms)
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for s in words:
            if s == s[::-1]:
                return s
        return ""
