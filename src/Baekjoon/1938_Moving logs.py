"""
https://www.acmicpc.net/problem/1938
Using BFS
"""
#1. My Solution(124ms)
from collections import deque

# t == 1: vertical / t == 0: horizontal
# when rotate, 3x3 cells should be empty
# since we check 2 cells in check_not_rotate, check_rotate only need to check 4 edge cells
def check_rotate(y, x):
    for i in (-1, 1):
        for j in (-1, 1):
            if not check(y+i, x+j) or board[y+i][x+j] == '1':
                return False

    return True
    
def check_not_rotate(y, x, t):
    if t == 0:
        for i in (-1, 0, 1):
            if not check(y, x+i) or board[y][x+i] == '1':
                return False
    else:
        for i in (-1, 0, 1):
            if not check(y+i, x) or board[y+i][x] == '1':
                return False    
    
    return True
    
def check(y, x):
    return 0 <= y < n and 0 <= x < n


n = int(input())
board = []
starts = []
ends = []

for i in range(n):
    board.append(input().strip())
    for j in range(n):
        if board[i][j] == 'B':
            starts.append((i, j))
        elif board[i][j] == 'E':
            ends.append((i, j))

start = starts[1]
t_start = 0 if starts[0][0] == starts[1][0] else 1
end = ends[1]
t_end = 0 if ends[0][0] == ends[1][0] else 1

ans = float('inf')
q = deque([(start[0], start[1], t_start, 0)])
directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (0, 0)]
visited = [[[False] * 2 for _ in range(n)] for _ in range(n)]
visited[start[0]][start[1]][t_start] = True

while q:
    y, x, t, v = q.popleft()
    if y == end[0] and x == end[1] and t == t_end:
        ans = min(ans, v)
        break
    
    for d in range(5):
        ny, nx = y + directions[d][0], x + directions[d][1]
        nt = t ^ 1 if d == 4 else t
        if check(ny, nx) and not visited[ny][nx][nt] and check_not_rotate(ny, nx, nt):
            if d < 4 or check_rotate(ny, nx):
                q.append((ny, nx, nt, v+1))
                visited[ny][nx][nt] = True

print(0 if ans == float('inf') else ans)
