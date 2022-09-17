"""
https://leetcode.com/problems/length-of-last-word/
Using list comprehension
"""
#1. My Solution (25ms)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len([x for x in s.split(" ") if len(x) > 0][-1])
    
#2. Other Solution
class Solution(object):
    def lengthOfLastWord(self, s):

        mystr = s.split()
        return len(mystr[-1])
