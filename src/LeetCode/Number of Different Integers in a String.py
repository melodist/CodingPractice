"""
https://leetcode.com/problems/number-of-different-integers-in-a-string/
Using regular expression
"""
#1. My Solution (77ms)
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(set([int(n) for n in re.compile('[0-9]+').findall(word)]))
    
#2. Other Solution (26ms)
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = set()
        tmp = ""
        
        for c in word:
            if c.isdigit():
                tmp += c
            else:
                if len(tmp) > 0:
                    s.add(int(tmp))
                    tmp = ""
        if len(tmp) > 0:
            s.add(int(tmp))
                    
        return len(s)
