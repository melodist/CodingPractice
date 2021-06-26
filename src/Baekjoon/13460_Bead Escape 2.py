"""
https://www.acmicpc.net/problem/13460
Using BFS
"""
#1. My Solution (100ms)
from collections import deque
import sys


def move(b, r, di, dj):
    bi, bj = b
    ri, rj = r
    
    nbi, nbj = b
    nri, nrj = r
    
    blue_in_the_hole = False
    red_in_the_hole = False
    
    while True:
        move_b = False
        move_r = False
        
        # Blue moves
        if 0 <= nbi+di < n and 0 <= nbj+dj < m:
            if board[nbi+di][nbj+dj] == 'O': 
                blue_in_the_hole = True
                break
            
            elif board[nbi+di][nbj+dj] != '#':
                nbi += di
                nbj += dj
                move_b = True
            
        # Red moves
        if 0 <= nri+di < n and 0 <= nrj+dj < m and not red_in_the_hole:
            if board[nri+di][nrj+dj] == 'O': 
                nri += di
                nrj += dj
                red_in_the_hole = True

            elif board[nri+di][nrj+dj] != '#':
                nri += di
                nrj += dj
                move_r = True
                
        # Check overlap
        if nbi == nri and nbj == nrj:
            nbi -= di * move_b
            nbj -= dj * move_b
            nri -= di * move_r
            nrj -= dj * move_r
            break
        
        # Check moved
        if not move_b and not move_r:
            break
        
    if blue_in_the_hole:
        return bi, bj, ri, rj
    else:
        return nbi, nbj, nri, nrj
    
input = sys.stdin.readline
n, m = map(int, input().split())
board = []

for i in range(n):
    board.append(input())
    for j in range(m):
        if board[i][j] == 'B':
            b = (i, j)
        elif board[i][j] == 'R':
            r = (i, j)
        elif board[i][j] == 'O':
            o = (i, j)

ans = -1
q = deque([(b, r, 0)])
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
visited[b[0]][b[1]][r[0]][r[1]] = True

while q:
    b, r, c = q.popleft()
    
    # Check if red in the hole
    if r[0] == o[0] and r[1] == o[1]:
        ans = c
        break
    
    # And then check if number of moves is 10.
    # If should be after the answer check
    if c == 10:
        continue

    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        bi, bj, ri, rj = move(b, r, di, dj)
        if not visited[bi][bj][ri][rj]:
            q.append(((bi, bj), (ri, rj), c+1))
            visited[bi][bj][ri][rj] = True

print(ans)
