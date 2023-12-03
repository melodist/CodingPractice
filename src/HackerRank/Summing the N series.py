"""
https://www.hackerrank.com/challenges/summing-the-n-series
Mathematical Problem
"""
#1. My Solution
def summingSeries(n):
    return n ** 2 % (10 ** 9 + 7)
