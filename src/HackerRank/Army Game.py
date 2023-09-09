"""
https://www.hackerrank.com/challenges/game-with-cells/problem
Mathematical Problem
"""
#1. My Soltuion
def gameWithCells(n, m):
    return math.ceil(n / 2) * math.ceil(m / 2)
