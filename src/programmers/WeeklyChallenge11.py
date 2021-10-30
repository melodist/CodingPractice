"""
https://programmers.co.kr/learn/courses/30/lessons/87694
Using BFS
"""
#1. My Solution
from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    def check(y, x, d):
        dy = [-1, 0, 1, 0]
        dx = [0, -1, 0, 1]
        ny = y*2 + dy[d]
        nx = x*2 + dx[d]

        if 0 < y <= 50 and 0 < x <= 50:
            if border[y*2][x*2] == 1 and border[ny][nx] == 1:
                return True

        return False
    
    # (y, x)가 도형의 내부에 있을 경우 True 반환
    def check_in(y, x):
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        
        # 8개의 점 중 1개만 0이어도 (y, x)는 도형의 테두리
        for k in range(8):
            by = y+dy[k]
            bx = x+dx[k]
            if 0 <= by < 103 and 0 <= bx < 103 and board[by][bx] == 0:
                return False
                
        return True

    board = [[0] * 103 for _ in range(103)] # (50, 50) 테두리 판정 위한 padding 추가 
    border = [[0] * 103 for _ in range(103)] # 격자 2배로 확대하여 ㄷ자 모양 체크
    visited = [[False] * 51 for _ in range(51)]
    
    # 사각형 채우기
    for lx, ly, rx, ry in rectangle:
        for c in range(lx*2, rx*2+1):
            for r in range(ly*2, ry*2+1):
                board[r][c] = 1

    # 테두리만 남기기
    for r in range(103):
        for c in range(103):
            if board[r][c] == 1 and not check_in(r, c):
                border[r][c] = 1
                
    q = deque([(characterY, characterX, 0)])
    visited[characterY][characterX] = True
    
    while q:
        y, x, d = q.popleft()
        if y == itemY and x == itemX:
            return d
        
        dy = [1, 0, -1, 0]
        dx = [0, 1, 0, -1]
        
        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if check(ny, nx, k) and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, d+1))
