"""
https://www.acmicpc.net/problem/1967
Using BFS
"""
#1. My Soltuion
import sys
from collections import defaultdict, deque


tree = defaultdict(dict)
n = int(input())
for _ in range(n-1):
    a, b, w = map(int, sys.stdin.readline().strip().split())
    tree[a][b] = w
    tree[b][a] = w

# Find furthest point p1 from root
q = deque([(1, 0)])
p, dist1 = 0, 0
visited = set()
while q:
    cur, d = q.popleft()
    if d > dist1:
        p = cur
        dist1 = d
        
    for u in tree[cur]:
        if u not in visited:
            q.append((u, d+tree[cur][u]))
            
    visited.add(cur)

# Find furthest point p2 from p1 and find distance between p1-p2
q = deque([(p, 0)])
p, dist2 = 0, 0
visited = set()
while q:
    cur, d = q.popleft()
    if d > dist2:
        p = cur
        dist2 = d
        
    for u in tree[cur]:
        if u not in visited:
            q.append((u, d+tree[cur][u]))
            
    visited.add(cur)
    
print(dist2)
