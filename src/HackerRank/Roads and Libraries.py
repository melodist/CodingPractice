"""
https://www.hackerrank.com/challenges/torque-and-development/problem
Using union-set algorithm
"""
#1. Solution using union-set
def roadsAndLibraries(n, c_lib, c_road, cities):
    def find_set(x):
        if root[x] == x:
            return x
        return find_set(root[x])

    if c_lib < c_road:
        return c_lib * n

    root = [i for i in range(n+1)]
    count = [1] * (n+1)
    graph = defaultdict(list)
    for u, v in cities:
        u_root = find_set(u)
        v_root = find_set(v)
        if u_root == v_root:
            continue
            
        root[v_root] = u_root
        count[u_root] += count[v_root]
        count[v_root] = 0

    num_lib = len([i for i, x in enumerate(root) if i == x]) - 1
    num_road = sum(count) - num_lib - 1
    return c_lib * num_lib + c_road * num_road
    
#2. Solution using BFS
from collections import defaultdict, deque


def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return c_lib * n

    root = [i for i in range(n+1)]
    count = [1] * (n+1)
    graph = defaultdict(list)
    for u, v in cities:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n+1)
    num_lib = 0
    num_road = 0
    for i in range(1, n+1):
        if not visited[i]:
            num_lib += 1
            visited[i] = True
            q = deque([i])
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if not visited[v]:
                        num_road += 1
                        q.append(v)
                        visited[v] = True

    return c_lib * num_lib + c_road * num_road
