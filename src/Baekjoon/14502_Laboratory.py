"""
https://www.acmicpc.net/problem/14502
Implementation Problem
"""
#1. My Solution
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
board = []
blanks = []
virus = []

for i in range(n):
    a = [*map(int, input().split())]
    for j in range(m):
        if a[j] == 0:
            blanks.append(i*m + j)
        elif a[j] == 2:
            virus.append(i*m + j)
            
    board.append(a)

def check(y, x):
    return 0 <= y < n and 0 <= x < m and board[y][x] == 0
    
def bfs():
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    infected = 0
    visited = [[False] * m for _ in range(n)]

    q = deque(virus)
    while q:
        u = q.popleft()
        y, x = divmod(u, m)
        visited[y][x] = True
        
        for dy, dx in dirs:
            if check(y+dy, x+dx) and not visited[y+dy][x+dx]:
                q.append((y+dy)*m + (x+dx))
                visited[y+dy][x+dx] = True
                infected += 1
        
    return infected
    
ans = 0
count = 0
viruses = len(virus)
walls = n * m - len(blanks) - viruses + 3

for c in combinations(blanks, 3):
    for u in c:
        y, x = divmod(u, m)
        board[y][x] = 1
    
    temp = n * m - bfs() - walls - viruses
    if temp > ans:    
        ans = temp

    for u in c:
        y, x = divmod(u, m)
        board[y][x] = 0
        
print(ans)
