"""
https://www.hackerrank.com/challenges/drawing-book/problem
Implementation Problem
"""
#1. My Solution
def pageCount(n, p):
    return min((n-p+1)//2, p//2) if n % 2 == 0 else min((n-p)//2, p//2)
