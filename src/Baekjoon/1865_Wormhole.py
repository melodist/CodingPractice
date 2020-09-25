"""
https://www.acmicpc.net/problem/1865
Using Bellman-Ford's algorithm
"""
#1. My Solution
import sys
from collections import defaultdict


def check():
    dist = [sys.maxsize] * (n+1)
    dist[1] = 0
    
    for v in range(1, n):  # Edge relaxtation for n-1 time
        for i in range(1, n+1):  # This means edge relaxation for all edges
            for u in graph[i]:
                dist[u] = min(dist[u], dist[i] + adj[i][u])
            
    for i in range(1, n+1):
        for u in graph[i]:
            if dist[u] > dist[i] + adj[i][u]:  # Find negative cycle
                return 'YES'
                
    return 'NO'


for _ in range(int(input())):
    n, m, w = map(int, sys.stdin.readline().strip().split())
    graph = defaultdict(set)
    adj = [[sys.maxsize] * (n+1) for _ in range(n+1)]

    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().strip().split())
        adj[s][e] = min(adj[s][e], t)
        adj[e][s] = adj[s][e]
        graph[s].add(e)
        graph[e].add(s)
    
    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().strip().split())
        adj[s][e] = -t
        graph[s].add(e)

    print(check())

#2. Solution using list
import sys
T = int(sys.stdin.readline())
def solve_bf(bf, graph, N, M):
    bf[1] = 0
    for it in range(N):
        for v in range(1, N+1):
            for nv, nw in graph[v]:
                if bf[nv] > bf[v] + nw:
                    bf[nv] = bf[v] + nw
                    if it == N-1:
                        print("YES")
                        return
    print("NO")
    return

for _ in range(T):
    N, M, W = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    bf = [1e9] * (N+1)
    for _ in range(M):
        s, e, t = map(int, sys.stdin.readline().split())
        graph[s].append([e, t])
        graph[e].append([s, t])
    for _ in range(W):
        s, e, t = map(int, sys.stdin.readline().split())
        graph[s].append([e, -t])
    solve_bf(bf, graph, N, M)
