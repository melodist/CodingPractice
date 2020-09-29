"""
https://www.acmicpc.net/problem/2206
Using BFS and store two cases for each point
"""
#1. My Solution
import sys
from collections import deque


def check(r, c):
    return 0 <= r < n and 0 <= c < m
    
    
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append([*map(int, list(sys.stdin.readline().strip()))])

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
q = deque([(0, 0, 1, 0)])
visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = True
visited[0][0][1] = True
flag = False
while q:
    r, c, dist, wall = q.popleft()
    if r == n - 1 and c == m - 1:
        print(dist)
        flag = True
        break
    
    for dr, dc in d:
        if check(r+dr, c+dc) and not visited[r+dr][c+dc][wall]:
            if arr[r+dr][c+dc] == 0:
                q.append((r+dr, c+dc, dist+1, wall))
                visited[r+dr][c+dc][wall] = True
            elif wall == 0:
                q.append((r+dr, c+dc, dist+1, 1))
                visited[r+dr][c+dc][1] = True
    
if not flag: print(-1)

#2. Other Solution
import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    q = deque()
    q.append([0, 0, 1])
    visit = [[[0] * 2 for i in range(m)] for i in range(n)]
    visit[0][0][1] = 1
    while q:
        a, b, w = q.popleft()
        if a == n - 1 and b == m - 1:
            return visit[a][b][w]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m:
                if s[x][y] == 1 and w == 1:
                    visit[x][y][0] = visit[a][b][1] + 1
                    q.append([x, y, 0])
                elif s[x][y] == 0 and visit[x][y][w] == 0:
                    visit[x][y][w] = visit[a][b][w] + 1
                    q.append([x, y, w])
    return -1
n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, list(input().strip()))))
print(bfs())
