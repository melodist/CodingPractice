"""
https://www.acmicpc.net/problem/18405
Implementation Problem
"""
#1. My Solution (100ms)
import sys


input = sys.stdin.readline
n, k = map(int, input().split())

board = []
for _ in range(n):
    board.append([*map(int, input().split())])
    
s, x, y = map(int, input().split())
dist = [401] * (k+1)


for i in range(n):
    for j in range(n):
        d = abs(x-i-1) + abs(y-j-1)
        if d <= s and board[i][j] > 0:
            dist[board[i][j]] = min(dist[board[i][j]], d)

print(dist.index(min(dist)))
