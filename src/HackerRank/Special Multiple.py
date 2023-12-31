"""
https://www.hackerrank.com/challenges/special-multiple
Mathematical Problem
Find answer using brute force. 9, 90, 99, 900, ...
"""
#1. My Solution
def solve(n):
    i = 1
    while (True):
        X = int(bin(i)[2:].replace('1', '9'))
        if X % n == 0:
            return str(X)
        i += 1
