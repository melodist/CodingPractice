"""
https://www.acmicpc.net/problem/14938
Using dijkstra
"""
#1. Solution using dijkstra (84ms)
import sys
import heapq


input = sys.stdin.readline
n, m, r = map(int, input().split())
items = [*map(int, input().split())]
graph = [{} for _ in range(n+1)]
ans = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l
    
for i in range(1, n+1):
    dist = [sys.maxsize] * (n+1)
    hq = [(0, i)]
    dist[i] = 0
    
    while hq:
        d, u = heapq.heappop(hq)
        for v in graph[u]:
            if dist[v] > d + graph[u][v]:
                dist[v] = d + graph[u][v]
                heapq.heappush(hq, (dist[v], v))
    
    temp = 0                
    for j in range(1, n+1):
        if dist[j] <= m:
            temp += items[j-1]
    
    ans = max(ans, temp)
    
print(ans)

#2. Solution using floyd-warshall (152ms)
import sys


input = sys.stdin.readline
n, m, r = map(int, input().split())
items = [*map(int, input().split())]
graph = [{} for _ in range(n+1)]
dists = [[987654321] * (n+1) for _ in range(n+1)]
ans = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    dists[a][b] = l
    dists[b][a] = l


for k in range(1, n+1):
    dists[k][k] = 0
    for i in range(1, n+1):
        if dists[i][k] == 987654321:
            continue
        for j in range(1, n+1):
            dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])
    
for i in range(1, n+1):
    temp = 0                
    for j in range(1, n+1):
        if dists[i][j] <= m:
            temp += items[j-1]
    
    ans = max(ans, temp)
    
print(ans)
