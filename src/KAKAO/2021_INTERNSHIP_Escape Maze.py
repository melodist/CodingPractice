"""
https://programmers.co.kr/learn/courses/30/lessons/81304
Using dijkstra and bit mask
Store state of graph in visited
"""
import heapq


def solution(n, start, end, roads, traps):
    n_traps = len(traps)
    tnums = [0] * (n+1)
    adj = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    for i, t in enumerate(traps):
        tnums[t] = 1 << i

    graph = [set() for _ in range(n + 1)]
    for p, q, s in roads:
        graph[p].add(q)
        graph[q].add(p)
        adj[p][q] = min(adj[p][q], s)

    # Store state of graph
    visited = [[float('inf')] * (2 ** n_traps) for _ in range(n + 1)]

    hq = [(0, start, 0)]
    answer = float('inf')

    while hq:
        dist, u, g = heapq.heappop(hq)
        if u == end:
            answer = min(answer, dist)
            continue

        for v in graph[u]:
            # Confirm each point is trap
            tu = g & tnums[u]
            tv = g & tnums[v]
            
            ng = g ^ tnums[v] if tnums[v] > 0 else g
            
            # If two points are activated or two points are not activated, it goes forward
            if (tu and tv) or (not tu and not tv):
                nd = adj[u][v]
            elif (not tu and tv) or (tu and not tv):
                nd = adj[v][u]

            if visited[v][ng] > dist + nd:
                visited[v][ng] = dist + nd
                heapq.heappush(hq, (dist + nd, v, ng))

    return answer
