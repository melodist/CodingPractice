"""
https://www.acmicpc.net/submit/1197
Using Prim Algorithm
1. Put 1 vertex in tree
2. Find node which has minimuim weight between (vertex in tree) - (vertex not in tree)
3. Repeat 2 until all vertices are in tree
"""
import sys
import heapq
from collections import deque


input = sys.stdin.readline
v, e = map(int, input().split())
adj = [{} for _ in range(v+1)]
visited = [False] * (v+1)
ans = 0
q = deque([1])

for i in range(e):
    a, b, c = map(int, input().split())
    if b in adj[a]:
        adj[a][b] = min(c, adj[a][b])
        adj[b][a] = min(c, adj[a][b])
    else:
        adj[a][b] = c
        adj[b][a] = c
        
hq = []    
while q:
    u = q.popleft()
    visited[u] = True
    
    for k in adj[u]:
        if not visited[k]:
            heapq.heappush(hq, (adj[u][k], k))
        
    while hq:
        w, v = heapq.heappop(hq)
        if not visited[v]:
            q.append(v)
            visited[v] = True
            ans += w
            break
        
print(ans)
