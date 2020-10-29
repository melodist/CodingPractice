"""
https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3
Using BFS
"""
#1. Failed Solution
# Fail if case has duplicated tickets
# [["ICN", "A"], ["ICN", "A"], ["A", "ICN"], ["A", "ICN"]]
# >> ["ICN", "A", "ICN", "A", "ICN"]
from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
        
    for k in graph:
        graph[k].sort(reverse=True)
        
    stack = [('ICN', set(), ["ICN"])]
    while stack:
        u, visited, route = stack.pop()
        if len(route) == len(tickets) + 1:
            return route
        
        for v in graph[u]:
            if (u, v) not in visited:
                stack.append((v, visited | set([(u, v)]), route + [v]))

#2. Collect Solution
from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
        
    for k in graph:
        graph[k].sort(reverse=True)
        
    st = ['ICN']
    answer = []
    while st:
        top = st[-1]
        
        if top not in graph or len(graph[top]) == 0:
            answer.append(st.pop())
        else:
            st.append(graph[top][-1])
            graph[top].pop()

    return answer[::-1]
