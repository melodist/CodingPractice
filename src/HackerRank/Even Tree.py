"""
https://www.hackerrank.com/challenges/even-tree/problem
Graph Theory
Using BFS to find parent of each node
Calculate total nodes that each subtree has
Find the number of subtree which has even number nodes
"""
from collections import defaultdict, deque


def evenForest(t_nodes, t_edges, t_from, t_to):
    parent = [-1] * t_nodes
    nodes = [1] * t_nodes
    tree = defaultdict(list)

    for i in range(t_edges):
        tree[t_from[i]].append(t_to[i])
        tree[t_to[i]].append(t_from[i])

    q = deque([1])
    stack = []
    parent[0] = 0
    while q:
        cur = q.popleft()
        stack.append(cur)
        for child in tree[cur]:
            if parent[child-1] == -1:
                parent[child-1] = cur
                q.append(child)

    while stack:
        c = stack.pop()
        while parent[c-1] != 0:
            p = parent[c-1]
            nodes[p-1] += 1
            c = parent[c-1]

    return len([x for x in nodes[1:] if x % 2 == 0])
