"""
https://www.acmicpc.net/problem/13549
Using BFS
"""
#1. My Solution
import sys
from collections import deque


n, k = map(int, input().split())
q = deque([(n, 0)])
MAX = 100001
visited = set([n])

while q:
    cur, t = q.popleft()
    if cur == k:
        print(t)
        break
    
    if 2 * cur < MAX and 2 * cur not in visited:
        visited.add(2 * cur)
        q.append((2*cur, t))
    for x in [cur-1, cur+1]:
        if 0 <= x < MAX and x not in visited:
            visited.add(x)
            q.append((x, t + 1))
            
#2. Other Solution using recursion
def BOJ13549():
    def c(n,k):
        if n>= k:
            return n-k
        elif k == 1:  # n == 0, k == 1
            return 1
        elif k % 2:  # k % 2 == 1
            return 1 + min(c(n, k-1), c(n, k+1))
        else:  # k % 2 == 0
            return min(k-n, c(n,k//2))
    n, k = map(int,input().split())
    print(c(n,k))
BOJ13549()
