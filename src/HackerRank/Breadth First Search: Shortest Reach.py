"""
https://www.hackerrank.com/challenges/bfsshortreach
Using BFS
"""
from collections import defaultdict, deque


def bfs(n, m, edges, s):
    # Make a tree
    tree = defaultdict(set)
    for a, b in edges:
        tree[a].add(b)
        tree[b].add(a)
    
    answer = [-1] * (n-1) # The node outside the tree will have -1
    level = [-1] * n # level < 0 : not visited
    level[s-1] = 0
    
    # BFS
    q = deque([s])
    while q:
        cur = q.popleft()
        for node in tree[cur]:
            if level[node-1] < 0:
                q.append(node)
                pos = node - 1 if node < s else node - 2
                level[node-1] = level[cur-1] + 1
                answer[pos] = level[node-1] * 6
                
        # visited[cur-1] = 1 <- If nodes makes a graph, this code will fail
                
    return answer
