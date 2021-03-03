"""
https://programmers.co.kr/learn/courses/30/lessons/72415?language=python3
Using BFS
1. Total cases = 6! = 360
2. 1-A -> 1-B // 2-A -> 2-B // ... ?
"""
from itertools import permutations
from collections import deque

def solution(board, r, c):
    def check(i, j):
        return 0 <= i < 4 and 0 <= j < 4
    
    def bfs(start, end):
        (a, b), (c, d) = start, end
        visited = [[-1] * 4 for _ in range(4)]
        visited[a][b] = 0
        q = deque([(a, b, 0)])
        ans = float('inf')
        while q:
            y, x, count = q.popleft()
            if y == c and x == d:
                ans = min(ans, count)
                continue
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if check(y+dy, x+dx) and visited[y+dy][x+dx] == -1:
                    q.append((y+dy, x+dx, count+1))
                    visited[y+dy][x+dx] = count+1
            
        return ans
    
    cards = [[] for _ in range(7)]
    num_cards = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                cards[board[i][j]].append((i, j))
                num_cards = max(num_cards, board[i][j])
    
    for p in permutations(range(1, num_cards+1), num_cards):
        # A -> XA / A -> XB
        temp = 0
        
        for k in range(2):
            
            answer = min(answer, temp)
    return answer
