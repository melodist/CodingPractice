"""
https://www.hackerrank.com/challenges/primsmstsub/problem
Prim's Algorithm - Greedy Algorithm Based
시작 정점을 선택한 후 정점에 인접한 간선중 최소 간선으로 연결된 정점을 선택하고, 
해당 정점에서 다시 최소 간선으로 연결된 정점을 선택하는 방식으로 최소 신장 트리를 확장
Using heap and adjacency list
"""
from collections import defaultdict


def prims(n, edges, start):
    # Make adjacency list
    graph = defaultdict(list)
    for a, b, w in edges:
        graph[a].append((w, a, b))
        graph[b].append((w, b, a))
    
    answer = 0
    
    # Select Start node
    connected_nodes = set([start])
    candidate_edge_list = graph[start]
    heapq.heapify(candidate_edge_list)
    
    while candidate_edge_list:
        weight, n1, n2 = heapq.heappop(candidate_edge_list)
        # Find minimal edge which has node in tree and node not in tree
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            answer += weight
            
            for edge in graph[n2]:
                if edge[2] not in connected_nodes:
                    heapq.heappush(candidate_edge_list, edge)

    return answer
