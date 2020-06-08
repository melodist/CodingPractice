"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
"""
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return (Counter(s) | Counter(t)) - (Counter(s) & Counter(t)) == {}
