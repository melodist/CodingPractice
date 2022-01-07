"""
https://www.acmicpc.net/problem/1916
Using Dijkstra
"""
#1. My Solution (392ms)
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
    if d[cur] < dist:
        continue
    for b, w in graph[cur]:
        new_d = dist + w
        if new_d < d[b]:
            d[b] = new_d
            heapq.heappush(hq, (new_d, b))
    
print(d[end])

#2. Other Solution (212ms)
import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def solve():
    n = int(input())
    m = int(input())

    adj = [dict() for _ in range(n+1)]

    for _ in range(m):
        s, e, c = map(int, input().split())
        if e in adj[s]:
            adj[s][e] = min(adj[s][e], c)
        else:
            adj[s][e] = c

    start, end = map(int, input().split())

    def dijkstra():
        dist = [sys.maxsize for _ in range(n+1)]
        dist[start] = 0
        hq = [(0, start)]
        while hq:
            cost, now = heappop(hq)
            if dist[now] < cost:
                continue
            if now==end:
                print(cost)
                exit()
            for nxt, ncost in adj[now].items():
                ncost += cost
                if dist[nxt] > ncost:
                    dist[nxt] = ncost
                    heappush(hq, (ncost, nxt))
    dijkstra()


if __name__ == '__main__':
    solve()
