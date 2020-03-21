"""
https://programmers.co.kr/learn/courses/30/lessons/1844
최단 경로만 찾으면 되기 때문에 그래프를 만들지 않고 BFS 실행
"""
def check(maps, x, y):
    m = len(maps)
    n = len(maps[0])

    return 0 <= x < n and  0 <= y < m and maps[y][x] == 1

def bfs(maps, start):
    dirs = [[1,0],[-1,0],[0,1],[0,-1]]
    m = len(maps)
    n = len(maps[0])

    queue = [start]
    result = []
    visited = []

    while queue:
        x, y, count = queue.pop(0)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if nx == n - 1 and  ny == m - 1:
                return count + 1
            elif check(maps, nx, ny):
                maps[ny][nx] = 0
                queue.append((nx, ny, count+1))

    return -1

def solution(maps):
    return bfs(maps, (0,0,1))
