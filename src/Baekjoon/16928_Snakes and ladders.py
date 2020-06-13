"""
https://www.acmicpc.net/problem/16928
Dictionary Comprehension using input()
"""
from collections import deque

n, m = map(int, input().split())
path = { k : v for k, v in (map(int, input().split()) for _ in range(n+m)) }

q = deque([(1, 0)])
visited = [0] * 101
visited[1] = 1

while q:
    cur, p = q.popleft()
    if cur == 100:
        print(p)
        break
    
    if cur in path:
        visited[cur] = 1
        cur = path[cur]
        
    for i in range(6):
        if cur+i+1 <= 100 and visited[cur+i+1] == 0:
            q.append((cur+i+1, p+1))
            visited[cur+i+1] = 1
