"""
https://programmers.co.kr/learn/courses/30/lessons/49191
Using 2 BFS and directed graph
"""
#1.My Solution
from collections import defaultdict, deque


def solution(n, results):
    answer = 0
    count = [0] * (n+1)
    graph1 = defaultdict(list)
    graph2 = defaultdict(list)
    for win, lose in results:
        graph1[win].append(lose)
        graph2[lose].append(win)

    for i in range(1, n+1):
        q = deque([i])
        visited = set([i])
        while q:
            u = q.popleft()
            for v in graph1[u]:
                if v not in visited:
                    count[v] += 1
                    q.append(v)
                    visited.add(v)

        q = deque([i])
        visited = set([i])
        while q:
            u = q.popleft()
            for v in graph2[u]:
                if v not in visited:
                    count[v] += 1
                    q.append(v)
                    visited.add(v)
    print(count)
    return count.count(n-1)
