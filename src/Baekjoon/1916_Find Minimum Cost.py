"""
https://www.acmicpc.net/problem/1916
Using Dijkstra
"""
#1. My Solution
# defaultdict raises memory overflow because of hash table
import sys
import heapq


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, w = map(int, sys.stdin.readline().strip().split())
    graph[a].append([b, w])
    
start, end = map(int, input().split())
d = [float('inf')] * (n+1)
d[start] = 0
hq = []
heapq.heappush(hq, (0, start))

while hq:
    dist, cur = heapq.heappop(hq)
    for b, w in graph[cur]:
        new_d = dist + w
        if new_d < d[b]:
            d[b] = new_d
            heapq.heappush(hq, (new_d, b))
    
print(d[end])
