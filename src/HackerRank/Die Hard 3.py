"""
https://www.hackerrank.com/challenges/die-hard-3
Mathematical Problem
"""
#1. My Solution
def solve(a, b, c):
    gcd = math.gcd(a,b)
    if c <= max(a,b) and c % gcd == 0:
          return "YES"
    return "NO"
