"""
https://www.hackerrank.com/challenges/tower-breakers-1/problem
Using game theory
Case #1. m == 1
P2 always wins
Case #2. n is even, n = 2k
P1 eliminates i = 1, 3, ..., 2k-1
P2 eliminates i = 2, 4, ..., 2k
P2 always wins
Case #3. n is odd, n = 2k + 1
P1 eliminates i = 1, 3, ..., 2k+1
P2 eliminates i = 2, 4, ..., 2k
P1 always wins
"""
#1. My Solution
def towerBreakers(n, m):
    return 2 if m == 1 or n % 2 == 0 else 1
