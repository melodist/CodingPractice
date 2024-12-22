"""
https://www.hackerrank.com/challenges/grid-challenge
Greedy Problem
"""
#1. My Solution
def gridChallenge(grid):
    h = len(grid)
    w = len(grid[0])
    
    for x in range(h):
        grid[x] = sorted(grid[x])
                
    for y in range(w):
        for x in range(h-1):
            if grid[x][y] > grid[x+1][y]:
                return 'NO'
    
    return 'YES'
