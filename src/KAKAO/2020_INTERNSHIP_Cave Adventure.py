"""
https://programmers.co.kr/learn/courses/30/lessons/67260
Using BFS to make directed graph and cycle detection using DFS
"""
#1. Failed Solution
# Cannot detect cycle by 3+ orders
from collections import defaultdict, deque


def solution(n, path, order):
    graph = defaultdict(list)
    graph_leaf = {}
    
    roots = [-2] * n
    level = [0] * n
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)
        
    q = deque([0])
    roots[0] = -1
    while q:
        cur = q.popleft()
        for u in graph[cur]:
            if roots[u] == -2:
                roots[u] = cur
                level[u] = level[cur] + 1
                q.append(u)
    
    for x, y in order:
        graph_leaf[y] = x
        
        temp = x
        if level[temp] > level[y]:
            i = level[temp] - level[y]
            while i > 0:
                temp = roots[temp]
                i -= 1
                
            # y is parent of temp
            if temp == y:
                return False
                
        # In (x, y) (c, d)
        # x is leaf of d and c is leaf of y
        # x -> root[x] find d
        # d -> c / check c is leaf of y
        temp = x
        while temp != 0:
            temp = roots[temp]
            if temp in graph_leaf:
                c = graph_leaf[temp]
                if level[c] > level[y]:
                    i = level[c] - level[y]
                    while i > 0:
                        c = roots[c]
                        i -= 1
                    if c == y:
                        return False     
    
    return True
    
#2. Correct Solution
from collections import defaultdict, deque


class Graph():
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.V = n

    def initialize(self, graph, order):
        q = deque([0])
        visited = set()
        while q:
            cur = q.popleft()
            for u in graph[cur]:
                if u not in visited:
                    self.graph[cur].append(u)
                    q.append(u)
            visited.add(cur)

        for a, b in order:
            self.graph[a].append(b)

    def is_cyclic(self):
        visited = set()
        on_stack = [False] * self.V
        
        # Since all nodes are guaranteed to be connected, use only 1 DFS
        st = [0]
        while st:
            cur = st[-1]

            if cur in visited:
                on_stack[cur] = False
                st.pop()
            else:
                visited.add(cur)
                on_stack[cur] = True

            for i in self.graph[cur]:
                if i not in visited:
                    st.append(i)
                elif on_stack[i]:
                    return False

        return True


def solution(n, path, order):
    graph = defaultdict(list)

    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    g = Graph(n)
    g.initialize(graph, order)

    return g.is_cyclic()
