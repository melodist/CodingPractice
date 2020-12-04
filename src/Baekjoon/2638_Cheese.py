"""
https://www.acmicpc.net/problem/2638
Using BFS to seperate inner air and outer air
"""
#1. My Solution (1920ms)
import sys
from collections import deque

def check(i, j):
    return i < n and j < m


input = sys.stdin.readline
n, m = map(int, input().split())
board = []
time = 0

for _ in range(n):
    board.append([*map(int, input().split())])
    
while True:
    # BFS
    q = deque([(0, 0)])
    cheese = 0
    cnt = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while q:
        u, v = q.popleft()
        for du, dv in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            if check(u+du, v+dv):
                if board[u+du][v+dv] == 1:
                    cnt[u+du][v+dv] += 1
                    cheese += 1
                elif not visited[u+du][v+dv]:
                    q.append((u+du, v+dv))
                visited[u+du][v+dv] = True

    for i in range(1, n):
        for j in range(1, m):
            if cnt[i][j] > 1:
                board[i][j] = 0
                
    if cheese == 0:
        break
    time += 1
    
print(time)

#2. Other Solution (104ms)
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
candidate = []
for i in range(M):
    if area[0][i] == 0:
        area[0][i] = 2
        candidate.append([0, i])
    if area[N-1][i] == 0:
        area[N-1][i] = 2
        candidate.append([N-1, i])
for i in range(1, N-1):
    if area[i][0] == 0:
        area[i][0] = 2
        candidate.append([i, 0])
    if area[i][M-1] == 0:
        area[i][M-1] = 2
        candidate.append([i, M-1])

time = 4
while candidate:
    time += 1
    candidate1 = []
    for x, y in candidate:
        important = False
        for dx, dy in zip(dxs, dys):
            x1 = x + dx
            y1 = y + dy
            if 0 <= x1 <= N-1 and 0 <= y1 <= M-1:
                if area[x1][y1] == 0:
                    area[x1][y1] = 2
                    candidate.append([x1, y1])
                elif area[x1][y1] == 1:
                    area[x1][y1] = time
                elif area[x1][y1] != 2:
                    candidate1.append([x1, y1])

    if candidate1:
        for x, y in candidate1:
            area[x][y] = 2
        candidate = candidate1

    else:
        print(time-5)
        break
