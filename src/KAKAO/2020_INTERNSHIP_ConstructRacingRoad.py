"""
https://programmers.co.kr/learn/courses/30/lessons/67259
"""
#1. Solution Using BFS
from collections import deque


def solution(board):
    def check(y, x):
        return 0 <= x < n and 0 <= y < n and board[y][x] == 0
    
    n = len(board)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    costs = [{'h':100, 'v':600}, {'h':600, 'v':100}]
    # Store the costs and check visited cell
    maps = [[0] * n for _ in range(n)]
    
    # initialize
    init = []
    if board[0][1] == 0:
        init.append((0, 1, 100, 'h'))
        maps[0][1] = 100
        
    if board[1][0] == 0:
        init.append((1, 0, 100, 'v'))
        maps[1][0] = 100
        
    q = deque(init)
    answer = float('inf')
    while q:
        y, x, cost, d = q.popleft()
        if y == n-1 and x == n-1:
            answer = min(answer, cost)
        else:
            for dy, dx in directions:
                if check(y+dy, x+dx):
                    new_cost = cost + costs[dy][d]
                    if maps[y+dy][x+dx] == 0 or maps[y+dy][x+dx] >= new_cost:
                        # while road is horizontal and next road is horzontal
                        # dy = 0
                        maps[y+dy][x+dx] = new_cost
                        d_next = 'h' if dy == 0 else 'v'
                        q.append((y+dy, x+dx, new_cost, d_next))
    
    return answer
    
#2. Solution Using Dijkstra
# Make Minimum Heap and push the edge for minimal costs
# Note that road has two directions, so result should be stored in 3D array
import heapq


def solution(board):
    def check(y, x):
        return 0 <= y < n and 0 <= x < n and board[y][x] == 0
    
    answer = 0
    n = len(board)
    costs = [[[float('inf')] * 2 for _ in range(n)] for _ in range(n)]
    costs[0][0][0] = 0
    costs[0][0][1] = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    c = [[100, 600], [600, 100]]
    hq = []
    
    # Initialize
    if board[0][1] == 0:
        heapq.heappush(hq, (100, 0, 1, 0))
        costs[0][1][0] = 100
    if board[1][0] == 0:
        heapq.heappush(hq, (100, 1, 0, 1))
        costs[1][0][1] = 100
        
    # d = 0 -> horizontal / d = 1 -> vertical
    while hq:
        cost, y, x, d = heapq.heappop(hq)
        for dy, dx in directions:
            new_d = abs(dy)
            new_cost = costs[y][x][d] + c[new_d][d]
            if check(y+dy, x+dx) and costs[y+dy][x+dx][new_d] >= new_cost:
                costs[y+dy][x+dx][new_d] = new_cost
                
                heapq.heappush(hq, (new_cost, y+dy, x+dx, new_d))
    
    return min(costs[n-1][n-1])
