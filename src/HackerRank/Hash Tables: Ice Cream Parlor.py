"""
https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem
Using hash table
"""
#1. My Solution
from collections import Counter


def whatFlavors(cost, money):
    flavors = {}
    count = Counter(cost)
    for c, m in enumerate(cost, 1):
        flavors[m] = c
    
    for c, m in enumerate(cost[:-1], 1):
        if m == money // 2 and count[m] < 2:
            continue
        if money - m in flavors:
            print(c, flavors[money - m]) if c < flavors[money - m] else print(flavors[money - m], c)
            return
