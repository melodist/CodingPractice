"""
https://www.acmicpc.net/problem/4386
Using Kruskal Algorithm
"""
#1. My Solution (124ms)
import heapq

n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]

adj = [[0] * n for _ in range(n)]
hq = []
for i in range(n):
    for j in range(n):
        adj[i][j] = ((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)**0.5
        heapq.heappush(hq, (adj[i][j], i+1, j+1))
        
ans = 0
root = [0] * (n+1)

while hq:
    dist, u, v = heapq.heappop(hq)
    
    while root[u] != 0:
        u = root[u]
        
    while root[v] != 0:
        v = root[v]
        
    if u != v:
        ans += dist
        root[v] = u
        
print(ans)

#2. Other Solution (64ms)
def find(n):
    if p[n] < 0:
        return n
    p[n] = find(p[n])
    return p[n]

def merge(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    p[b] = a
import sys
from itertools import combinations as comb
input = sys.stdin.readline
N = int(input())
s = []
stars = []
p = [-1] * N
for i in range(N):
    stars.append(list(map(float, input().split())))
for s1, s2 in comb([x for x in range(N)], 2):
    x1,y1 = stars[s1]
    x2,y2 = stars[s2]
    s.append((((y2-y1)**2+(x2-x1)**2)**0.5,s1, s2))
c = 0
for cost, a, b in sorted(s):
    if find(a) == find(b):
        continue
    merge(a, b)
    c += cost
print(c)
