"""
https://www.hackerrank.com/challenges/countingsort4/problem
Using Counting Sort
"""
#1. My Solution
from functools import reduce


def countSort(arr):
    count = [[] for _ in range(100)]
    n = len(arr)
    for i, (x, s) in enumerate(arr):
        x = int(x)
        if i < n // 2:
            count[x].append('-')
        else:
            count[x].append(s)

    print(' '.join(reduce(lambda x, y: x+y, count)))
