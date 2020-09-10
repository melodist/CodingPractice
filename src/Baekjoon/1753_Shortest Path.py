"""
https://www.acmicpc.net/problem/1753
Using Dijkstra algorithm
"""
#1. My Solution
import sys
import heapq
from collections import defaultdict


V, E = map(int, input().split())
start = int(input())
adj = defaultdict(dict)  # Using dict not list because V <= 20,000
graph = defaultdict(set)  
d = [float('inf')] * (V+1)
d[start] = 0

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    if v not in adj[u]:
        adj[u][v] = w
    else:
        adj[u][v] = min(adj[u][v], w)
    graph[u].add(v)
    
# Can optimize with hq = [(0, start)]    
hq = []  # Using priority queue
for i in range(V):  
    if start == i+1:
        heapq.heappush(hq, (0, start))
    else:
        heapq.heappush(hq, (float('inf'), i+1))

visited = [False] * (V+1)
while hq:
    dist, cur = heapq.heappop(hq)
    assert cur <= V
    
    if visited[cur]:
        continue
    
    for u in graph[cur]:
        d[u] = min(d[u], dist + adj[cur][u])
        heapq.heappush(hq, (d[u], u))  # Not need to push distance which is not minimum
    
    visited[cur] = True

[print(i) if i != float('inf') else print('INF') for i in d[1:]]

#2. Other Solution
import sys
import heapq
input =sys.stdin.readline
INF = sys.maxsize

def solve():
    V, E = map(int, sys.stdin.readline().split())
    K = int(sys.stdin.readline())
    
    adj = [dict() for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        if v in adj[u]:
            adj[u][v] = min(adj[u][v],w)
        else:
            adj[u][v] = w
    
    dist = [INF for _ in range(V + 1)]
    dist[K] = 0
    q = [(0, K)]
    
    while q:
        c, p = heapq.heappop(q)
        if c > dist[p]:
            continue
        for v, w in adj[p].items():
            if dist[v] <= c+w:
                continue
            dist[v] = c+w
            heapq.heappush(q, (c+w, v))
    
    for r in dist[1:]:
        if r < sys.maxsize:
            print(r)
        else:
            print("INF")
        
if __name__=='__main__':
    solve()
