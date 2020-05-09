"""
https://www.acmicpc.net/problem/13913
방문한 노드의 부모를 기록해 두고 목표 지점 도달시 기록한 부모를 이용하여 경로를 찾음.
"""
from collections import deque

n, k = map(int, input().split())

LIMIT = 100001
parent = [-1] * LIMIT

q = deque([n])

while q:
    cur = q.popleft()
    if cur == k:
        path = [cur]
        while cur != n:
            path.append(parent[cur])
            cur = parent[cur]
        break
    for p in (cur+1, cur-1, cur*2):
        if 0 <= p <= LIMIT - 1 and parent[p] == -1:
            parent[p] = cur
            q.append(p)

print(len(path) - 1)
print(' '.join(map(str, path[::-1])))
