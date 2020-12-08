"""
https://www.acmicpc.net/problem/11779
Using dijkstra
"""
#1. My Solution (296ms)
import sys
import heapq


input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [{} for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    if v not in graph[u] or graph[u][v] > w:
        graph[u][v] = w
    
a, b = map(int, input().split())

hq = [(a, 0)]
dist = [sys.maxsize] * (n+1)
dist[a] = 0
route = [0] * (n+1)

while hq:
    u, d = heapq.heappop(hq)
    
    if d > dist[u]:
        continue
    
    for v in graph[u]:
        if graph[u][v] + d < dist[v]:
            dist[v] = graph[u][v] + d
            heapq.heappush(hq, (v, dist[v]))
            route[v] = u

print(dist[b])

node = b
path = []
while node:
    path.append(node)
    node = route[node]
    
print(len(path))
[print(p, end=' ') for p in path[::-1]]

#2. Other Solution (236ms)
import sys
import heapq

input = sys.stdin.readline
flush = sys.stdout.flush

n = int(input())
m = int(input())
nbhd = [[] for _ in range(n + 1)]
parent = [None] * (n + 1)
for _ in range(m):
	a, b, c = map(int, input().split())
	nbhd[a].append((c, b))

start, end = map(int, input().split())
dist = [10**10 + 1] * (n + 1)
dist[start] = 0
pq = [(0, start)]
while pq:
	d, i = heapq.heappop(pq)
	if dist[i] != d:
		continue
	if i == end:
		break
	for e, j in nbhd[i]:
		if e + d < dist[j]:
			dist[j] = e + d
			parent[j] = i
			heapq.heappush(pq, (dist[j], j))

path = [end]
while path[-1] != start:
	path.append(parent[path[-1]])
print(dist[end])
print(len(path))
print(*reversed(path))
