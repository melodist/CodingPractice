"""
https://www.hackerrank.com/challenges/sherlock-and-permutations
Mathematical Problem
"""
#1. My Solution
def solve(n, m):
    if m == 1:
        return 1
    return math.factorial(n+m-1) // (math.factorial(n) * math.factorial(m-1)) % (10**9 + 7)
