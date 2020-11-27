"""
https://programmers.co.kr/learn/courses/30/lessons/68937?language=python3#
Using BFS
Answer should be D (Diameter is not unique) or D-1 (Diameter is unique)
If diameter of tree (d1-d2) is unique, we can get answer by selecting d1, d2 and neighbor point of d1
"""
#1. My Solution
from collections import deque, defaultdict


def solution(n, edges):
    def bfs(s):
        q = deque([s])
        dist = [-1] * (n+1)
        dist[s] = 0
        d_max = v_max = 0
        while q:
            u = q.popleft()
            for v in tree[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
                    if d_max < dist[v]:
                        v_max = [v]
                        d_max = dist[v]
                    elif d_max == dist[v]:
                        v_max.append(v)

        return v_max, d_max
    
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
              
    v1, d1 = bfs(1)
    v1 = v1[0]
    
    # Find diameter of tree
    v2, d2 = bfs(v1)
    if len(v2) > 1:
        return d2
    
    # Find another diameter of tree from another point
    v2 = v2[0]
    v3, d3 = bfs(v2)
    return d3 if len(v3) > 1 else d3-1
