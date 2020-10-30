"""
https://programmers.co.kr/learn/courses/30/lessons/49190?language=python3#
Using BFS
"""
#1. My Soltuion
from collections import deque


def solution(arrows):
    answer = 0
    dir_x = [0, 1, 1, 1, 0, -1, -1, -1]
    dir_y = [1, 1, 0, -1, -1, -1, 0, 1]
    
    check, visited = {}, {}
    q = deque([(0, 0)])
    
    x, y, px, py = 0, 0, 0, 0
    for a in arrows:
        for j in range(2):  # Find diagonal intersection by extend plane
            x += dir_x[a]
            y += dir_y[a]

            check[(x, y)] = 0
            visited[(x, y, px, py)] = 0
            visited[(px, py, x, y)] = 0
            q.append((x, y))
            px, py = x, y

    px, py = q.popleft()
    check[(px, py)] = 1
    
    while q:
        x, y = q.popleft()
        if check[(x, y)] == 1:
            if visited[(x, y, px, py)] == 0:
                answer += 1
                visited[(x, y, px, py)] = 1
                visited[(px, py, x, y)] = 1
        else:
            check[(x, y)] = 1
            visited[(x, y, px, py)] = 1
            visited[(px, py, x, y)] = 1
            
        px, py = x, y
            
    return answer
