"""
https://www.acmicpc.net/problem/2239
Using Backtracking
"""
#1. My Solution (6444ms)
import sys


def dfs(n):
    if n == 81:
        [print(''.join(map(str, r))) for r in board]
        return True
    
    r = n // 9
    c = n % 9
    
    if board[r][c] > 0:
        return dfs(n+1)
    else:
        for i in range(1, 10):
            if not row[r][i] and not col[c][i] and not cell[r // 3 * 3 + c // 3][i]:
                row[r][i] = col[c][i] = cell[r // 3 * 3 + c // 3][i] = True
                board[r][c] = i
                if dfs(n+1):
                    return True
                row[r][i] = col[c][i] = cell[r // 3 * 3 + c // 3][i] = False
                board[r][c] = 0
                
    return False
    

input = sys.stdin.readline
board = [[*map(int, input().strip())] for _ in range(9)]
# row[i][v] means value v with ith row is determined
row = [[False] * 10 for _ in range(10)]
col = [[False] * 10 for _ in range(10)]
cell = [[False] * 10 for _ in range(10)]
for i in range(9):
    for j in range(9):
        if board[i][j] > 0:
            row[i][board[i][j]] = col[j][board[i][j]] = cell[i // 3 * 3 + j // 3][board[i][j]] = True
dfs(0)
