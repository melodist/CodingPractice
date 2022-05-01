"""
https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/
Implementation Problem
"""
#1. My Solution
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        removed = []
        for i, c in enumerate(number):
            if c == digit:
                removed.append(number[:i] + number[i+1:])
                
        print(removed)
        removed.sort(key=lambda x: int(x), reverse=True)
        return removed[0]

#2. Other Solution
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        l=[]
        for i in range(len(number)):
            if number[i]==digit:
                l.append(int(number[:i]+number[i+1:]))
        return str(max(l))
