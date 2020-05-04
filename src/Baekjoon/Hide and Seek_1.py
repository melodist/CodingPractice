"""
https://www.acmicpc.net/problem/1697
1. queue.Queue()는 collections.deque에 비하여 아주 느림 (https://www.acmicpc.net/board/view/49166)
2. 방문할 node를 추가하는 순서에 유의 (ex. n = 0, k = 10)
"""
from collections import deque

n, k = map(int, input().split())
q = deque([n])
visited = [0] * 100001

while q:
    cur = q.popleft()
    if cur == k:
        print(visited[cur])
        break
    else:
        for i in (cur + 1, cur - 1, cur * 2):
            if 0 <= i <= 100000 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[cur] + 1
