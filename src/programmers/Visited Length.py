"""
https://programmers.co.kr/learn/courses/30/lessons/49994?language=python3
Using hash
"""
#1. My Solution
from collections import deque


def solution(dirs):
    direction = {"L" : (-1, 0), "R" : (1, 0), "D" : (0, -1), "U" : (0, 1)}
    answer = 0
    visited = set()
    x = y = 0
    
    for d in dirs:
        dx, dy = direction[d]
        nx = x+dx
        ny = y+dy
        
        if nx > 5 or nx < -5 or ny > 5 or ny < -5:
            continue
        t = (nx, x, ny, y) if d == 'L' or d == 'U' else (x, nx, y, ny) 
            
        if t not in visited:
            answer += 1
            visited.add(t)
        x, y = nx, ny
        
    return answer
