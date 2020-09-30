"""
https://www.acmicpc.net/problem/11404
Using Floyd-Warshall
"""
#1. My Solution
import sys


n = int(input())
m = int(input())

dist = [[sys.maxsize] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if dist[a][b] > c:
        dist[a][b] = c
    
for i in range(1, n+1):
    dist[i][i] = 0
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                
                
for r in dist[1:]:
    ans = ''
    for i in r[1:]:
        ans += '0 ' if i == sys.maxsize else str(i) + ' '
    print(ans)
