"""
https://leetcode.com/problems/is-graph-bipartite/
Using BFS
Divide nodes for two sets, set with zero and set not with zero
"""
#1. My Solution (222ms)
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:   
        def bfs(start):
            queue = deque([start])
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    check_and_append(queue, u, v)
            
        def initialize_used():
            used = [[True] * n for _ in range(n)]
            for i in range(n):
                for j in graph[i]:
                    used[i][j] = False
            return used
        
        def check_and_append(queue, u, v):
            if u in with_start:
                if not used[u][v] and not v in with_start:
                    used[u][v] = used[v][u] = True
                    not_with_start.add(v)
                    queue.append(v)
            else:
                if not used[u][v] and not v in not_with_start:
                    used[u][v] = used[v][u] = True
                    with_start.add(v)
                    queue.append(v)
        
        def check(used):
            for i in range(n):
                for j in range(n):
                    if not used[i][j]:
                        return False
                    
            return True
        
        n = len(graph)
        with_start = set()
        not_with_start = set()
        used = initialize_used()
        
        with_start.add(0)
            
        [bfs(i) for i in range(n)] # Find cases for cutted graph
        
        return check(used)

#2. Other Solution using DFS (164ms)
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = color[node] ^ 1 # Store inverse color for node using XOR / 0^1 = 1, 1^1 = 0
                        elif color[nei] == color[node]:
                            return False
        return True
