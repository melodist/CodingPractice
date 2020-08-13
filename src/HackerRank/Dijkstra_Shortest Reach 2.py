"""
https://www.hackerrank.com/challenges/dijkstrashortreach/problem
"""
import heapq


def shortestReach(n, edges, s):
    adj = [{} for _ in range(n+1)]
    dist = [float('inf')] * (n+1)
    
    for a, b, d in edges:
        if b in adj[a]:
            adj[a][b] = min(d, adj[a][b])
        else:
            adj[a][b] = d

        if a in adj[b]:
            adj[b][a] = min(d, adj[b][a])
        else:
            adj[b][a] = d
    
    heap = []
    heapq.heappush(heap, [s, 0])
    dist[s] = 0

    while heap:
        current_node, current_dist = heapq.heappop(heap)

        for adj_node, adj_dist in adj[current_node].items():
            
            next_dist = current_dist + adj_dist

            if next_dist < dist[adj_node]:
                dist[adj_node] = next_dist
                heapq.heappush(heap, [adj_node, next_dist])

    dist = [-1 if x == float('inf') else x for x in dist]

    return dist[1:s] + dist[s+1:]
