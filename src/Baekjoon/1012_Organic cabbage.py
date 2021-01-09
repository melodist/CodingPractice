"""
https://www.acmicpc.net/problem/1012
Using BFS
"""
#1. My Solution (104ms)
import sys
from collections import deque


input = sys.stdin.readline
def check(i, j):
    return 0 <= i < n and 0 <= j < m and g[i][j] == 1
    

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    g = [[0] * m for _ in range(n)]
    cab = []
    for _ in range(k):
        x, y = map(int, input().split())
        cab.append((y, x))
        g[y][x] = 1
        
    visited = [[False] * m for _ in range(n)]
    ans = 0
    for i, j in cab:
        if visited[i][j]:
            continue
        ans += 1
        q = deque([(i, j)])
        while q:
            u, v = q.popleft()
            for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if check(u+dy, v+dx) and not visited[u+dy][v+dx]:
                    visited[u+dy][v+dx] = True
                    q.append((u+dy, v+dx))
                    
    print(ans)
