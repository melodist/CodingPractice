"""
https://www.acmicpc.net/problem/2252
Using Toplogical Sort
"""
#1. My Soltuion (264ms)
import sys
from collections import deque

def dfs(s):
    zero = []
    for u in adj[s]:
        conn[u] -= 1
        if conn[u] == 0:
            zero.append(u)
            
    return zero

input = sys.stdin.readline
n, m = map(int, input().split())
adj = [[] * (n+1) for _ in range(n+1)]
conn = [0] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    conn[v] += 1
    
# Find start which conn[s] == 0
q = deque([])
for i in range(1, n+1):
    if conn[i] == 0:
        q.append(i)

ans = []
while q:
    s = q.popleft()
    ans.append(str(s))
    q += dfs(s)
    
print(' '.join(ans))

#2. Other Solution (200ms)
import heapq
import io
import os
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def topologicalSort():
    n, m = map(int, input().split())
    number = [0 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        number[b] += 1
    que = []
    for i in range(1, n+1):
        if number[i] == 0:
            heapq.heappush(que, i)
    res = []
    for i in range(n):
        tmp = heapq.heappop(que)
        res.append(tmp)
        for p in graph[tmp]:
            number[p] -= 1
            if number[p] == 0:
                heapq.heappush(que, p)
    sys.stdout.write(' '.join(map(str,res)))


if __name__ == '__main__':
    topologicalSort()
