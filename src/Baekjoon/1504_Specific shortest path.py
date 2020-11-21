"""
https://www.acmicpc.net/problem/1504
Using Dijkstra
"""
#1. My Solution
import sys
import heapq

def solve():
    def dijkstra(start, v1, v2):
            
        hq = [(start, 0)]
        dists = [sys.maxsize] * (n+1)
        dists[start] = 0
        
        while hq:
            u, d = heapq.heappop(hq)
            for v in graph[u]:
                if dists[v] > d + graph[u][v]:
                    dists[v] = d + graph[u][v]
                    heapq.heappush(hq, (v, dists[v]))

        return dists[v1], dists[v2]
    
    input = sys.stdin.readline
    n, e = map(int, input().strip().split())
    graph = [{} for _ in range(n+1)]
    for _ in range(e):
        u, v, c = map(int, input().strip().split())
        graph[u][v] = c
        graph[v][u] = c
    
    v1, v2 = map(int, input().strip().split())
    
    d_a, d_b = dijkstra(1, v1, v2)
    d_c, d_c = dijkstra(v1, v2, v2)
    d_d, d_e = dijkstra(n, v1, v2)

    ans = min(d_a + d_c + d_e, d_b + d_c + d_d)
    return ans if ans < sys.maxsize else -1
    
print(solve())

#2. Other Solution
import sys
from heapq import heappop, heappush
from collections import defaultdict as dd
from math import inf
input = sys.stdin.readline

n, e = map(int, input().split())
path = [dd(lambda: inf) for i in range(n+1)]
for i in range(e):
    a, b, c = map(int, input().split())
    path[a][b] = c
    path[b][a] = c

v1, v2 = map(int, input().split())


def dist(a, b):
    from_a = dd(lambda: inf)
    from_a[a] = 0
    que = [(0, a)]
    res = {}
    while que:
        di, i = heappop(que)
        if di > from_a[i]:
            continue
        if i in b:
            b.remove(i)
            res[i] = di
            if not b:
                return res
        for j, k in path[i].items():
            dj = di + k
            if dj < from_a[j]:
                from_a[j] = dj
                heappush(que, (dj, j))
    return inf

y1 = dist(v1, {1, v2, n})
if y1 == inf:
    print(-1)
else:
    y2 = dist(v2, {1, n})
    print(y1[v2] + min(y1[1]+y2[n], y1[n]+y2[1]))
