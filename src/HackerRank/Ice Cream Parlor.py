"""
https://www.hackerrank.com/challenges/icecream-parlor/problem
"""
#1. Naive Solution
from collections import deque


def icecreamParlor(m, arr):
    i = 1
    arr = deque(arr)
    ans = []
    while arr:
        a = arr.popleft()
        for j, b in enumerate(arr):
            if a + b == m:
                return [i, i+j+1]
        i += 1

#2. O(n) Solution
from collections import defaultdict


def icecreamParlor(m, arr):
    freq = defaultdict(list)
    for i, a in enumerate(arr):
        freq[a].append(i+1)

    for i, a in enumerate(arr):
        b = m - a
        if a == b and len(freq[b]) > 1:
            return freq[b]
        elif a != b and len(freq[b]) > 0:
            return [i+1, freq[b][0]]
