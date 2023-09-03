"""
https://www.hackerrank.com/challenges/connecting-towns
Mathematical Problem
"""
#1. My Solution
def connectingTowns(n, routes):
    return functools.reduce(lambda acc, cur: acc * cur, routes, 1) % 1234567
