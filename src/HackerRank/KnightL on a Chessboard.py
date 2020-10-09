"""
https://www.hackerrank.com/challenges/knightl-on-chessboard/problem
Using BFS
"""
from collections import deque


def check(n, x, y):
    return 0 <= x < n and 0 <= y < n


def bfs(n, a, b):
    q = deque([(0, 0)])
    moves = [[-1] * n for _ in range(n)]
    moves[0][0] = 0
    move = [[a, b], [b, a], [a, -b], [b, -a],
    [-a, b], [-b, a], [-a, -b], [-b, -a]]
    while q:
        x, y = q.popleft()
        if x == n-1 and y == n-1:
            return moves[x][y]

        for dx, dy in move:
            if check(n, x+dx, y+dy) and moves[x+dx][y+dy] == -1:
                q.append((x+dx, y+dy))
                moves[x+dx][y+dy] = moves[x][y] + 1

    return -1
    
def knightlOnAChessboard(n):
    ans = [[0] * (n-1) for _ in range(n-1)]
    for a in range(1, n):
        for b in range(a, n):
            ans[a-1][b-1] = ans[b-1][a-1] = bfs(n, a, b)

    return ans
