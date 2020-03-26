"""
https://www.acmicpc.net/problem/11725
list를 통해 구현한 queue와 queue모듈에서 제공하는 Queue의 속도 차이
list.pop(0) -> O(n) / pop the element and move all the memory to the side
queue.get() -> O(1) / pop the element
"""
import queue
def bfs(s):
    q = queue.Queue()
    q.put(s)
    
    while queue:
        out = q.get(0)
        for node in tree[out]:
            if not visited[node]:
                visited[node] = True
                parent[node] = out
                q.put(node)

n = int(input())

parent = [0] * (n+1)
visited = [False] * (n+1)
visited[1] = True

tree = [[] for x in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    tree[b].append(a)
    tree[a].append(b)
    
bfs(1)

for i in range(n-1):
    print(parent[i+2])
