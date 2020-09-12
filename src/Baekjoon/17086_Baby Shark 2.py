"""
https://www.acmicpc.net/problem/17086
Using BFS (Breadth First Search)
"""
#1. My Solution
import sys
from collections import deque
from itertools import chain

n, m = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
answer = 0
def check(r, c):
    return 0 <= r < n and 0 <= c < m
    
directions = [[(a, b) for a in (-1, 0, 1)] for b in (-1, 0, 1)]
d = list(chain(*directions))

sharks = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            sharks.append((i, j))
            
q = deque(sharks)
while q:    
    visited = set()
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            if dr != 0 or dc != 0:
                if check(r+dr, c+dc) and arr[r+dr][c+dc] == 0:
                    q.append((r+dr, c+dc))
                    arr[r+dr][c+dc] = arr[r][c] + 1

print(max(map(max, arr)) - 1)

#2. Former Solution (Timeout in Python3)
import sys
from collections import deque
from itertools import chain

n, m = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
board = [[sys.maxsize] * m for _ in range(n)]
answer = 0
def check(r, c):
    return 0 <= r < n and 0 <= c < m
    

directions = [[(a, b) for a in (-1, 0, 1)] for b in (-1, 0, 1)]
d = list(chain(*directions))

sharks = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            sharks.append((i, j))
            
for i, j in sharks:
    q = deque([(i, j, 0)])
    visited = set()
    while q:
        r, c, dist = q.popleft()
        if arr[r][c] == 0:
            board[r][c] = min(board[r][c], dist)
        
        for dr, dc in d:
            if dr != 0 or dc != 0:
                if check(r+dr, c+dc) and arr[r+dr][c+dc] == 0 and (r+dr, c+dc) not in visited:
                    q.append((r+dr, c+dc, dist+1))
                    visited.add((r+dr, c+dc))
                
        visited.add((r, c))

answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] < sys.maxsize:
            answer = max(answer, board[i][j])

print(answer)
