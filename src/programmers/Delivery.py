"""
https://programmers.co.kr/learn/courses/30/lessons/12978
Using Dijkstra
"""
#1. My Solution
import heapq


def solution(N, road, K):
    visited = [float('inf')] * (N+1)
    adj = [[float('inf')] * (N+1) for _ in range(N+1)]
    tree = [set() for _ in range(N+1)]
    for a, b, c in road:
        adj[a][b] = adj[b][a] = min(adj[a][b], c)
        tree[a].add(b)
        tree[b].add(a)
    
    visited[1] = 0
    hq = [(0, 1)]
    while hq:
        d, u = heapq.heappop(hq)
        for v in tree[u]:
            if visited[v] > d + adj[u][v]:
                visited[v] = d + adj[u][v]
                heapq.heappush(hq, (d + adj[u][v], v))
    answer = 0
    for r in visited:
        if r <= K:
            answer += 1

    return answer
