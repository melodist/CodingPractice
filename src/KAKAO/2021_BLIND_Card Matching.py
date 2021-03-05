"""
https://programmers.co.kr/learn/courses/30/lessons/72415?language=python3
Using BFS
1. Total cases = 6! = 360
2. 1-A -> 1-B // 2-A -> 2-B // ... ?
"""
#1. My Solution
from itertools import permutations
from collections import deque

def solution(board, r, c):
    def find(start, i, p, b):
        board = [r[:] for r in b]
        
        def check(i, j):
            return 0 <= i < 4 and 0 <= j < 4
        
        def bfs(start, end):
            (a, b), (c, d) = start, end
            if start == end:
                return 0
            
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
                    if check(y+dy, x+dx) and visited[y+dy][x+dx] == -1: # 1step
                        q.append((y+dy, x+dx, count+1))
                        visited[y+dy][x+dx] = count+1
                    
                    # ctrl move
                    if dy == -1 and y > 1: 
                        for k in range(y-1, 0, -1):
                            if board[k][x] > 0:
                                if visited[k][x] == -1:
                                    q.append((k, x, count+1))
                                    visited[k][x] = count+1
                                break
                        else:
                            if visited[0][x] == -1:
                                q.append((0, x, count+1))
                                visited[0][x] = count+1
                        
                    if dy == 1 and y < 2:
                        for k in range(y+1, 3):
                            if board[k][x] > 0:
                                if visited[k][x] == -1:
                                    q.append((k, x, count+1))
                                    visited[k][x] = count+1
                                break
                        else: 
                            if visited[3][x] == -1:
                                q.append((3, x, count+1))
                                visited[3][x] = count+1
                            
                    if dx == -1 and x > 1:
                        for k in range(x-1, 0, -1):
                            if board[y][k] > 0:
                                if visited[y][k] == -1:
                                    q.append((y, k, count+1))
                                    visited[y][k] = count+1
                                break
                        else:
                            if visited[y][0] == -1:
                                q.append((y, 0, count+1))
                                visited[y][0] = count+1
                            
                    if dx == 1 and x < 2:
                        for k in range(x+1, 3):
                            if board[y][k] > 0:
                                if visited[y][k] == -1:
                                    q.append((y, k, count+1))
                                    visited[y][k] = count+1
                                break
                        else: 
                            if visited[y][3] == -1:
                                q.append((y, 3, count+1))
                                visited[y][3] = count+1   
            return ans
        
        # x -> ia -> ib -> y / x -> ib -> ia -> y
        if i == len(p):
            return 0
        v1 = bfs(start, cards[p[i]][0]) + bfs(cards[p[i]][0], cards[p[i]][1]) + 2
        v2 = bfs(start, cards[p[i]][1]) + bfs(cards[p[i]][1], cards[p[i]][0]) + 2
        y1,x1 = cards[p[i]][0]
        board[y1][x1] = 0
        y2,x2 = cards[p[i]][1]
        board[y2][x2] = 0
            
        return min(v1 + find(cards[p[i]][1], i+1, p, board), v2 + find(cards[p[i]][0], i+1, p, board))
    
    # Find card position
    cards = [[] for _ in range(7)]
    num_cards = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                cards[board[i][j]].append((i, j))
                num_cards = max(num_cards, board[i][j])

    answer = float('inf')
    for p in permutations(range(1, num_cards+1), num_cards):
        temp = find((r, c), 0, p, board)
        answer = min(answer, temp)
        
    return answer
