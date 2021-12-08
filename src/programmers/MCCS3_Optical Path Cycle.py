"""
https://programmers.co.kr/learn/courses/30/lessons/86052/
Using BFS
"""
#1. My Solution
from collections import deque


def solution(grid):
    def bfs(y, x, d):
        q = deque([(y, x, d)])
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        while q:
            y, x, d = q.popleft()

            if grid[y][x] == "L":
                nd = (d + 1) % 4
            elif grid[y][x] == "R":
                nd = (d + 3) % 4
            else:
                nd = d

            ny = (y + directions[nd][1] + r) % r
            nx = (x + directions[nd][0] + c) % c

            if visited[ny][nx][nd] == -1:
                visited[ny][nx][nd] = visited[y][x][d] + 1
                q.append((ny, nx, nd))
            else:
                return visited[y][x][d]

    r = len(grid)
    c = len(grid[0])
    visited = [[[-1] * 4 for _ in range(c)] for _ in range(r)]
    answer = []

    for i in range(r):
        for j in range(c):
            for d in range(4):
                if visited[i][j][d] == -1:
                    visited[i][j][d] = 1
                    answer.append(bfs(i, j, d))

    return sorted(answer)
