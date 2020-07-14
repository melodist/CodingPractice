"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/
"""
#1. My Solution using KMP
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        n = len(needle)
        m = len(haystack)
        
        if n > m:
            return -1
        
        f = [0] * n
        begin, matched = 1, 0
        while begin + matched < n:
            if needle[begin + matched] == needle[matched]:
                matched += 1
                f[begin + matched - 1] = matched
            else:
                if matched == 0:
                    begin += 1
                else:
                    begin += matched - f[matched - 1]
                    matched = f[matched - 1]
        
        print(f)
        
        ans = []
        cur, j = 0, 0
        while cur <= m - n:
            if j < n and haystack[cur+j] == needle[j]:
                j += 1
                if j == n:
                    return cur
            else:
                if j == 0:
                    cur += 1 
                else:
                    cur += j - f[j-1]
                    j = f[j-1]

        return -1
        
#2. Optimal Solution
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "": return 0
        return haystack.find(needle)
