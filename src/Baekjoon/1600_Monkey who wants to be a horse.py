"""
https://www.acmicpc.net/problem/1600
Using BFS
"""
#1. My Solution (pypy3 - 604ms)
import sys
from collections import deque

def check(x, y):
    return 0 <= x < w and 0 <= y < h and board[y][x] == 0

input = sys.stdin.readline
k = int(input())
w, h = map(int, input().split())
ans = float('inf')
board = []
visited = [[[False] * w for _ in range(h)] for _ in range(k+1)]  # cnt_horse, x, y
visited[0][0][0] = True

directions_monkey = [(1, 0), (0, 1), (-1, 0), (0, -1)]
directions_horse = [(-1, -2), (-2, -1),
                    (-1, 2), (-2, 1),
                    (1, -2), (2, -1),
                    (1, 2), (2, 1)]

for _ in range(h):
    board.append(list(map(int, input().split())))
    
q = deque([(0, 0, 0, 0)])  # cnt, cnt_horse, x, y
while q:
    cnt, cnt_horse, x, y = q.popleft()
    if x == w - 1 and y == h - 1:
        ans = min(ans, cnt)
        continue
    
    if cnt_horse < k:
        for dx, dy in directions_horse:
            if check(x+dx, y+dy) and not visited[cnt_horse+1][y+dy][x+dx]:
                q.append((cnt+1, cnt_horse+1, x+dx, y+dy))
                visited[cnt_horse+1][y+dy][x+dx] = True
                
                
    for dx, dy in directions_monkey:
        if check(x+dx, y+dy) and not visited[cnt_horse][y+dy][x+dx]:
            q.append((cnt+1, cnt_horse, x+dx, y+dy))
            visited[cnt_horse][y+dy][x+dx] = True
            
print(ans if ans < float('inf') else -1) 
