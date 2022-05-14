"""
https://leetcode.com/problems/network-delay-time/
Using BFS
"""
#1. My Solution (538ms)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def bfs(start):
            visited = dict()
            visited[start] = 0
            
            t = 0
            q = deque([start])
            
            while q:
                u = q.popleft()
                for v in edges[u]:
                    if v not in visited or visited[v] > visited[u] + edges[u][v]:
                        visited[v] = visited[u] + edges[u][v]
                        q.append(v)
            
            # Should visited all nodes
            # If all nodes were visited, find maximum delay time
            return -1 if len(visited) < n else max(visited.values())
        
        edges = [dict() for _ in range(n+1)]
        
        for u, v, w in times:
            edges[u][v] = w

        return bfs(k)
        
