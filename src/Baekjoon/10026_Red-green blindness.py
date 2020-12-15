"""
https://www.acmicpc.net/problem/10026
Using DFS
"""
#1. My Solution (120ms)
import sys
from collections import deque

def check(i, j, a):
    return 0 <= i < n and 0 <= j < n and visited[i][j] == -1

def dfs(i, j, a):
    q = deque([(i, j)])
    visited[i][j] = a
    while q:
        i, j = q.popleft()
        
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i+di, j+dj
            if check(ni, nj, a) and board[i][j] == board[ni][nj]:
                visited[ni][nj] = a
                q.append((ni, nj))

 
def dfs_weak(i, j, a):
    q = deque([(i, j)])
    visited[i][j] = a
    while q:
        i, j = q.popleft()
        
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i+di, j+dj
            if check(ni, nj, a) and board[ni][nj] in colors:
                visited[ni][nj] = a
                q.append((ni, nj))
    
    
board = []
n = int(input())
for r in sys.stdin.readlines():
    board.append(r.strip())


visited = [[-1] * n for _ in range(n)]
a = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == -1:
            dfs(i, j, a)
            a += 1

visited = [[-1] * n for _ in range(n)]
colors = set(['G', 'R'])
b = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == -1:
            if board[i][j] == 'B':
                dfs(i, j, b)
                b += 1
            else:
                dfs_weak(i, j, b)
                b += 1

print(a, b)

#2. Other Solution (72ms)
import sys
sys.setrecursionlimit(10**5)
n=int(input())
a=[[" "]*(n+2)]+[list(" "+input()+" ")for i in[0]*n]+[[" "]*(n+2)]  # zero-padding
b=[i.copy()for i in a]
def cnt(s,x,y,c):
    s[x][y]=" "
    if s[x-1][y]==c:cnt(s,x-1,y,c)
    if s[x+1][y]==c:cnt(s,x+1,y,c)
    if s[x][y-1]==c:cnt(s,x,y-1,c)
    if s[x][y+1]==c:cnt(s,x,y+1,c)
c=d=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if a[i][j]!=" ":
            cnt(a,i,j,a[i][j]);c+=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if b[i][j]=="G":b[i][j]="R"  # Change all G to R
for i in range(1,n+1):
    for j in range(1,n+1):
        if b[i][j]!=" ":
            cnt(b,i,j,b[i][j]);d+=1
print(c,d)
