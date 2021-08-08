"""
https://www.acmicpc.net/problem/2573
Implementation Problem
"""
#1. My Solution (1052ms in Pypy3)
# Timeout because this solution counts every cell in board
import sys
from collections import deque


def check(i, j):
    return 0 <= i < n and 0 <= j < m and board[i][j] > 0

def bfs(i, j, count):
    q = deque([(i, j)])
    visited[i][j] = count
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if check(r+dr, c+dc) and visited[r+dr][c+dc] == -1:
                visited[r+dr][c+dc] = count
                q.append((r+dr, c+dc))


input = sys.stdin.readline
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

time = 1
while True:
    # Glacier Melts
    board_next = [r[:] for r in board]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                # up
                if i > 0:
                    board_next[i-1][j] = max(0, board_next[i-1][j] - 1)
                # down
                if i < n-1:
                    board_next[i+1][j] = max(0, board_next[i+1][j] - 1)
                # left
                if j > 0:
                    board_next[i][j-1] = max(0, board_next[i][j-1] - 1)
                # right
                if j < m-1:
                    board_next[i][j+1] = max(0, board_next[i][j+1] - 1)
    
    board[:] = board_next[:]

    # Calc glacier
    visited = [[-1] * m for _ in range(n)]
    count = -1
    
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0 and visited[i][j] == -1:
                count += 1
                visited[i][j] = count
                bfs(i, j, count)
  
    if count == -1:
        print(0)
        break
    elif count > 0:
        print(time)
        break
    
    time += 1
    
#2. Other Solution (2700ms)
# Counts only iceberg cells
import sys

class IceBerg:

    piece = int()
    icePosition = []

    def __init__(self, n, m, ice):
        self.n = n
        self.m = m
        self.ice = ice

        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if self.ice[i][j] > 0:
                    self.icePosition.append([i, j])

    def icebergCount(self):
        ret = 0
        visit = [[False] * m for _ in range(n)]
        for i, j in self.icePosition:
            if visit[i][j] is False:
                ret += 1
                self.bfs(visit, i, j)

        self.piece = ret
        return ret

    def bfs(self, visit, y, x):
        qu = [[y, x]]
        visit[y][x] = True

        while len(qu):
            posy, posx = qu.pop()

            if self.ice[posy][posx - 1] > 0 and visit[posy][posx - 1] is False:
                visit[posy][posx - 1] = True
                qu.append([posy, posx - 1])
            if self.ice[posy][posx + 1] > 0 and visit[posy][posx + 1] is False:
                visit[posy][posx + 1] = True
                qu.append([posy, posx + 1])
            if self.ice[posy - 1][posx] > 0 and visit[posy - 1][posx] is False:
                visit[posy - 1][posx] = True
                qu.append([posy - 1, posx])
            if self.ice[posy + 1][posx] > 0 and visit[posy + 1][posx] is False:
                visit[posy + 1][posx] = True
                qu.append([posy + 1, posx])

    def melting(self):
        melt = []
        tmpPosition = []

        for i, j in self.icePosition:
            cnt = 0
            if self.ice[i][j - 1] == 0:
                cnt += 1
            if self.ice[i][j + 1] == 0:
                cnt += 1
            if self.ice[i - 1][j] == 0:
                cnt += 1
            if self.ice[i + 1][j] == 0:
                cnt += 1

            if cnt > 0:
                melt.append([i, j, cnt])
            else:
                tmpPosition.append([i, j])

        for i, j, cnt in melt:
            self.ice[i][j] -= cnt
            if self.ice[i][j] < 0:
                self.ice[i][j] = 0
            if self.ice[i][j] != 0:
                tmpPosition.append([i, j])

        self.icePosition = tmpPosition

n, m = map(int, sys.stdin.readline().split())
ice = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

iceberg = IceBerg(n, m, ice)
ans = 0

while iceberg.icebergCount() == 1:
    ans += 1
    iceberg.melting()

if iceberg.piece >= 2:
    print(ans)
else:
    print(0)
