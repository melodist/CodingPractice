"""
https://www.hackerrank.com/challenges/harry-potter-and-the-floating-rocks
Mathematics Problem
"""
#1. My Solution
def solve(x1, y1, x2, y2):
    if abs(x1 - x2) < abs(y1 - y2):
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    
    return math.gcd(abs(x2 - x1), abs(y2 - y1)) - 1
