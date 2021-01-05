"""
https://www.acmicpc.net/problem/2606
Using BFS
"""
#1. My Solution (88ms)
import sys
from collections import deque


input = sys.stdin.readline
n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(int(input())):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
    
q = deque([1])
ans = 0
visited = [False] * (n+1)
visited[1] = True
while q:
    u = q.popleft()
    for v in g[u]:
        if not visited[v]:
            ans += 1
            q.append(v)
            visited[v] = True
            
print(ans)

#2. Other Solution (52ms)
from sys import stdin
read = stdin.readline
dic={}
for i in range(int(read())):
    dic[i+1] = set()
for j in range(int(read())):
    a, b = map(int,read().split())
    dic[a].add(b)
    dic[b].add(a)

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)
visited = []
dfs(1, dic)
print(len(visited)-1)
