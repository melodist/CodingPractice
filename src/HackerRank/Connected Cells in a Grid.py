"""
https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem
Using DFS to make a cell and loop for whole matrix
Skip visited cell
"""
from collections import deque


def check(y, x):
    return (0 <= x < m and 0<= y < n)

def dfs(y, x, visited):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1), 
                    (1, 1), (1, -1), (-1, -1), (-1, 1)]
    q = deque([(y, x)])
    ret = 0

    while q:
        i, j = q.popleft()
        if (i, j) not in visited:
            for di, dj in directions:
                if check(i+di, j+dj) and matrix[i+di][j+dj] == 1:
                    q.append((i+di, j+dj))
            visited.add((i, j))
            ret += 1

    return ret


def connectedCell(matrix):
    n = len(matrix)
    m = len(matrix[0])
    visited = set()
    answer = 0
    
    for i in range(n):
        for j in range(m):
            if (i, j) not in visited and matrix[i][j] == 1:
                print(i, j)
                cells = dfs(i, j, visited)
                answer = max(cells, answer)

    return answer
