"""
Implementation Problem
"""
#1. My Solution
from functools import reduce


def solution(sizes):
    s = [(a, b) if a > b else (b, a) for a, b in sizes]
    return reduce(lambda x, y: max(x, y), [x[0] for x in s]) * reduce(lambda x, y: max(x, y), [x[1] for x in s])

#2. Other Solution
"""
def sum(values, start = 0):
    total = start
    for value in values:
        total = total + value
    return total
"""
solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)
