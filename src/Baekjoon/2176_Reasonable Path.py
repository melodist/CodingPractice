"""
https://www.acmicpc.net/problem/2176
Using tree dynamic programming
"""
#1. My Solution
import sys
import heapq


input = sys.stdin.readline
n, m = map(int, input().strip().split())
graph = [{} for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().strip().split())
    graph[a][b] = c
    graph[b][a] = c

d = [10**9] * (n+1)
dp = [0] * (n+1)
d[2] = 0; dp[2] = 1
hq = [(0, 2)]
while hq:
    dist, u = heapq.heappop(hq)
    if d[u] ^ dist:
        continue
    for v in graph[u]:
        dist_next = graph[u][v] + dist
        if dist_next < d[v]:
            d[v] = dist_next
            heapq.heappush(hq, (dist_next, v))
        if d[v] < dist:
            dp[u] += dp[v]
    
print(dp[1])
