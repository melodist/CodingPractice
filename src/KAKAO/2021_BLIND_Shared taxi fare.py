"""
https://programmers.co.kr/learn/courses/30/lessons/72413?language=python3
Using Djikstra
"""
#1. My Solution
import heapq


def solution(n, s, a, b, fares):
    d = [[float('inf')] * (n+1) for _ in range(n+1)]
    m = [{} for _ in range(n+1)]
    for u, v, t in fares:
        m[u][v] = t
        m[v][u] = t
        
    for i in range(1, n+1):
        hq = [(i, 0)]
        d[i][i] = 0
        while hq:
            u, dist = heapq.heappop(hq)
            for v in m[u]:
                if dist + m[u][v] < d[i][v]:
                    d[i][v] = dist + m[u][v]
                    heapq.heappush(hq, (v, d[i][v]))

    answer = float('inf')
    for k in range(1, n+1):
        answer = min(answer, d[s][k] + d[k][a] + d[k][b])
        
    return answer
