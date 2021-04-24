"""
https://www.acmicpc.net/problem/14500
Using DFS
"""
#1. Solution Using DFS (320ms)
import sys

def dfs(y, x, c, d):
    score = 0
    
    if c + max_value * (4-d) < ans:
        return 0
        
    if d == 4:
        return c
        
    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ny, nx = y+dy, x+dx
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            visited[ny][nx] = True
            if d == 2:
                score = max(score, dfs(y, x, board[ny][nx] + c, d+1))
            score = max(score, dfs(ny, nx, board[ny][nx] + c, d+1))
            visited[ny][nx] = False
    
    return score
    
input = sys.stdin.readline    
N, M = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(N)]
max_value = max(max(board))
visited = [[False] * M for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        ans = max(ans, dfs(i, j, board[i][j], 1))
        visited[i][j] = False
            
print(ans)

#2. Solution Using BFS - (1152ms in Pypy3)
# Rotate Board Instead of rotating blocks
from collections import deque
import sys

def check(y, x, r, c):
    return 0 <= y < r and 0 <= x < c
    
input = sys.stdin.readline    
N, M = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(N)]
blocks = [((0, 0), (0, 1), (0, 2), (0, 3)),
        ((0, 0), (0, 1), (1, 0), (1, 1)),
        ((0, 0), (1, 0), (2, 0), (2, 1)),
        ((0, 0), (1, 0), (1, 1), (2, 1)),
        ((0, 0), (0, 1), (1, 1), (0, 2))
        ]
        
ans = 0
for _ in range(4):
    board = [list(a[::-1]) for a in zip(*board)] # rotation
    for _ in range(2):
        board = [a[::-1] for a in board] # symmetry
    
        r, c = len(board), len(board[0])
        q = deque([(0, 0)])
        
        visited = [[False] * c for _ in range(r)]
        visited[0][0] = True
        while q:
            y, x = q.popleft()
            
            # calculate score
            for block in blocks:
                temp = 0
                flag = True
                for dy, dx in block:
                    ny, nx = y+dy, x+dx
                    if check(ny, nx, r, c):
                        temp += board[ny][nx]
                    else:
                        flag = False
                        break
                ans = max(ans, temp) if flag else ans
                    
            # find next cell
            for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ny, nx = y+dy, x+dx
                if check(ny, nx, r, c) and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
            
print(ans)
