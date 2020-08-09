"""
https://www.hackerrank.com/challenges/count-luck/problem
"""
#1. My Solution
from collections import deque


def check(matrix, x, y):
    n = len(matrix)
    m = len(matrix[0])
    return 0 <= x < m and 0 <= y < n and matrix[y][x] != 'X'

def countLuck(matrix, k):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    n = len(matrix)
    m = len(matrix[0])
    visited = [[True] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '*':
                end = (i, j)
            elif matrix[i][j] == 'M':
                start = (i, j)
    
    print(start, end)

    q = deque([(start, 0)])
    visited[start[0]][start[1]] = False

    while q:
        cur, count = q.popleft()
        if cur == end:
            return 'Impressed' if count == k else 'Oops!'

        temp = []
        for dx, dy in directions:
            if check(matrix, cur[1]+dx, cur[0]+dy) and \
                visited[cur[0]+dy][cur[1]+dx]:
                temp.append((cur[0]+dy, cur[1]+dx))

        if len(temp) > 1:
            count += 1

        for t in temp:
            q.append((t, count))

        visited[cur[0]][cur[1]] = False
