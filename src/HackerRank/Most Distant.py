"""
https://www.hackerrank.com/challenges/most-distant
Mathematical Problem
"""
#1. My Solution
def dist(a, b):
    return math.sqrt(a**2 + b**2)

def solve(coordinates):
    x, y = list(zip(*coordinates))
    x_max = max(x)
    x_min = min(x)
    y_max = max(y)
    y_min = min(y)
    
    dists = [dist(x_max, y_max), dist(x_max, y_min), x_max - x_min, dist(x_min, y_max), dist(x_min, y_min), y_max - y_min]
    return max(dists)
