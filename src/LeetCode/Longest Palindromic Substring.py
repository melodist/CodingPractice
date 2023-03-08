"""
https://leetcode.com/problems/longest-palindromic-substring
Using two pointer approach
"""
#1. My Solution (506ms)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l+1:r]

        ans = ""
        for i in range(len(s)):
            s1 = palindrome(s, i, i)
            s2 = palindrome(s, i, i+1)
            if len(ans) < len(s1):
                ans = s1

            if len(ans) < len(s2):
                ans = s2

        return ans
    
#2. Other Solution (80ms)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        start, size = 0, 1
        for i in range(1, len(s)):
            l, r = i - size, i + 1
            s1, s2 = s[l-1:r], s[l:r]
            if l >= 1 and s1 == s1[::-1]:
                size += 2
                start = l - 1
            elif s2 == s2[::-1]:
                size += 1
                start = l

        return s[start: start + size]
