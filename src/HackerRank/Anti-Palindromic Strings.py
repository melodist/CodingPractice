"""
https://www.hackerrank.com/challenges/antipalindromic-strings
Mathmatical Problem
Anti-palindromic string is a string that does not contain any palindromic substrings of the length of 2 and 3
"""
#1. My Solution
def solve(n, m):
    mod = 1000000007
    return m % mod if n == 1 else (pow(m-2, n-2, mod) * m * (m-1)) % mod
