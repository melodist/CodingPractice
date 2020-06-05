"""
https://programmers.co.kr/learn/courses/30/lessons/49189
Using BFS
"""
from collections import defaultdict, deque

def solution(n, edge):
    graph = defaultdict(list)
    dist = [-1] * (n+1)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    dist[1] = 0
    q = deque([1])
    while q:
        cur = q.popleft()
        for a in graph[cur]:
            if dist[a] == -1:
                q.append(a)
                dist[a] = dist[cur] + 1

    return dist.count(max(dist))
