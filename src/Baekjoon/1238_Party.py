"""
https://www.acmicpc.net/problem/1238
Using 2 Dijkstra
"""
#1. My Solution
import sys
import heapq
from collections import defaultdict


input = sys.stdin.readline
n, m, x = map(int, input().strip().split())
dists = [[0] * (n+1) for _ in range(n+1)]
dp = [sys.maxsize] * (n+1)
dp_rev = [sys.maxsize] * (n+1)
adj = defaultdict(set)
adj_rev = defaultdict(set)

for _ in range(m):
    u, v, t = map(int, input().strip().split())
    dists[u][v] = t
    adj[u].add(v)
    adj_rev[v].add(u)

# Forward Dijkstra (x to all)
hq = [(0, x)]
dp[x] = 0
while hq:
    d, u = heapq.heappop(hq)
    for v in adj[u]:
        if dp[v] > d + dists[u][v]:
            dp[v] = d + dists[u][v]
            heapq.heappush(hq, (dp[v], v))

# Reverse Dijkstra (All to x)
hq = [(0, x)]
dp_rev[x] = 0
while hq:
    d, u = heapq.heappop(hq)
    for v in adj_rev[u]:
        if dp_rev[v] > d + dists[v][u]:
            dp_rev[v] = d + dists[v][u]
            heapq.heappush(hq, (dp_rev[v], v))

ans = 0
for i in range(1, n+1):
    ans = max(ans, dp[i] + dp_rev[i])
    
print(ans)

#2. Other Solution
import sys
from heapq import *
input = sys.stdin.readline
n, m, x = map(int, input().split())
home = [[] for _ in range(n+1)]
home2 = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    home[s].append((e, t))
    home2[e].append((s, t))

def dijkstra(g, start):
    d=[9876543210]*(n+1)
    d[start] = 0
    heap = [(0,start)]
    while heap:
        total, node = heappop(heap)
        if d[node]<total:continue
        for nxt, cost in g[node]:
            if d[nxt]>d[node]+cost:
                d[nxt] = d[node]+cost
                heappush(heap, (d[nxt],nxt))
    return d[1:]

print(max([a+b for a, b in zip(dijkstra(home, x), dijkstra(home2,x))]))
