"""
https://www.hackerrank.com/challenges/filling-jars
Mathematical Problem
"""
#1. My Solution
def solve(n, operations):
    return math.floor(sum([k * (b - a + 1) for a, b, k in operations]) / n)
