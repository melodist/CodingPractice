"""
https://www.hackerrank.com/challenges/lowest-triangle
Mathematical Problem
"""
#1. My Solution
def lowestTriangle(trianglebase, area):
    return math.ceil(area * 2 / trianglebase)
