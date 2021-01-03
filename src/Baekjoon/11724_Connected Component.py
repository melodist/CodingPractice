"""
https://www.acmicpc.net/problem/11724
Using BFS
"""
#1. My Solution (900ms)
import sys
from collections import deque


def bfs(start):
    q = deque([start])
    while q:
        u = q.popleft()
        for v in g[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
                
input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
    
ans = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    if visited[i]:
        continue
    ans += 1
    bfs(i)
    
print(ans)
