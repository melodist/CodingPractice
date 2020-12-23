"""
https://www.acmicpc.net/problem/1987
Using BFS and backtracking
"""
#1. My Solution (1504ms)
r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
cache = [['' for _ in range(c)] for _ in range(r)]

def bfs(x, y):
    queue = [(x, y, board[x][y])]
    ans = 0
    while queue:
        x, y, path = queue.pop()
        chk = False  # Check board[x][y] is end
        for i, j in (1, 0), (-1, 0), (0, 1), (0, -1):
            xx, yy = x+i, y+j
            if xx < 0 or yy < 0 or xx >= r or yy >= c:
                continue
            if board[xx][yy] not in path:
                chk = True
                if cache[xx][yy] != path + board[xx][yy]:
                    cache[xx][yy] = path + board[xx][yy]
                    queue.append((xx, yy, path + board[xx][yy]))
        if not chk:
            ans = max(ans, len(path))
    return ans

print(bfs(0, 0))
