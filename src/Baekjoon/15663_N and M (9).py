"""
https://www.acmicpc.net/problem/15663
Using permutation and sort
"""
import sys
from itertools import permutations


n, m = map(int, input().split())
arr = input().split()
arr.sort(key=lambda x:int(x))  # Note that 16 < 135, '16' > '135'
answer = []
visited = set()

for p in permutations(arr, m):
    s = ' '.join(p)
    if s not in visited:
        answer.append(s)
        visited.add(s)
    
[print(c) for c in answer]
