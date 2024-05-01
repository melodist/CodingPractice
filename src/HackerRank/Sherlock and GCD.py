"""
https://www.hackerrank.com/challenges/sherlock-and-gcd
Mathematical Problem
"""
#1. My Solution
def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)
        
def solve(a):
    p = reduce(gcd, a)
    
    if (p == 1):
        return "YES"
    else:
        return "NO"
