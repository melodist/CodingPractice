"""
https://www.hackerrank.com/challenges/sherlock-and-moving-tiles
Mathematics Problem
"""
#1. My Solution
import math


def movingTiles(l, s1, s2, queries):
    times = []
    for q_i in queries:
      t = (l*math.sqrt(2) - math.sqrt(2*q_i))/abs(s1-s2)
      times.append(t)
    return times
