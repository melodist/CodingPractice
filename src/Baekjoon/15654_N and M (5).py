"""
https://www.acmicpc.net/problem/15654
"""
#1. Recursive Solution
import sys


n, m = map(int, input().split())
arr = [*map(int, sys.stdin.readline().strip().split())]
arr.sort()
visited = [False] * n

def select(a, k, visited):
    if k == m:
        print(' '.join(map(str, a)))
        return
    
    
    for i, x in enumerate(arr):
        if not visited[i]:
            visited[i] = True
            select(a + [x], k+1, visited)
            visited[i] = False
        
select([], 0, visited)

#2. Non-recursive Solution (Slower and heavier)
import sys
from collections import deque


n, m = map(int, input().split())
arr = [*map(int, sys.stdin.readline().strip().split())]
arr.sort()
arr = [*map(str, arr)]

q = deque([[]])
while q:
    a = q.popleft()
    if len(a) == m:
        print(' '.join(a))

    for x in arr:
        if x in set(arr) - set(a):
            q.append(a + [x])

#3. Other Solution
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
arr = map(str, arr)
print('\n'.join(list(map(' '.join, permutations(arr, M)))))
