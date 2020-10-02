"""
https://www.acmicpc.net/problem/1167
Using 2 BFS
"""
#1. My Solution
import sys
from collections import defaultdict, deque


v = int(input())
tree = defaultdict(dict)
for _ in range(v):
    s = [*map(int, sys.stdin.readline().strip().split())]
    u = s[0]
    i = 1
    while i < len(s) - 1:
        v = s[i]; w = s[i+1]
        tree[u][v] = w
        i += 2

# First BFS : Find furthest node from root
q = deque([(1, 0)])
visited = set([1])
target = dist = 0
while q:
    u, d = q.popleft()
    if d > dist:
        target = u
        dist = d
        
    for v in tree[u]:
        if v not in visited:
            q.append((v, d + tree[u][v]))
            visited.add(v)

# Second BFS : Find furthest node from target
q = deque([(target, 0)])
visited = set([target])
dist2 = 0
while q:
    u, d = q.popleft()
    if d > dist2:
        dist2 = d
        
    for v in tree[u]:
        if v not in visited:
            q.append((v, d + tree[u][v]))
            visited.add(v)
            
print(dist2)
