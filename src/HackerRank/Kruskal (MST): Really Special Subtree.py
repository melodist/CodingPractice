"""
https://www.hackerrank.com/challenges/kruskalmstrsub/problem
Using Kruskal Algorithm
Minimum Heap and Disjoint set
"""
import heapq


def kruskals(g_nodes, g_from, g_to, g_weight):
    root = [0] * (g_nodes + 1)
    heap = []
    g_edges = len(g_from)
    for i in range(g_edges):
        g_sum = g_weight[i] + g_from[i] + g_to[i]
        heapq.heappush(heap, (g_weight[i], g_sum, g_from[i], g_to[i]))
    

    answer = 0
    while heap:
        wt, _, u, v = heapq.heappop(heap)

        while root[u] != 0:
            u = root[u]

        while root[v] != 0:
            v = root[v]

        if u != v:
            answer += wt
            root[v] = u

    return answer
