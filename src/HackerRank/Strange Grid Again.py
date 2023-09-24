"""
https://www.hackerrank.com/challenges/strange-grid
Mathematical Problem
"""
#1. My Solution
def strangeGrid(r, c):
    return (r-1) // 2 * 10 + (r-1) % 2 + (c - 1) * 2
