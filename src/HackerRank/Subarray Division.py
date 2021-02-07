"""
https://www.hackerrank.com/challenges/the-birthday-bar/problem
Implementation Problem
"""
#1. My Solution
from itertools import accumulate


def birthday(s, d, m):
    ans = 0
    n = len(s)
    ss = [0] + list(accumulate(s))

    for i in range(len(ss)-m):
        if ss[i+m] - ss[i] == d:
            ans += 1
    
    return ans
    
#2. Other Solution
def getWays(squares, d, m):
    tp = (len(squares)-m) + 1 #total number of pieces possible
    return len([1 for i in range(tp) if sum(squares[i:i+m])==d])
