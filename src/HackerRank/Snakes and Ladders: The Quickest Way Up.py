"""
https://www.hackerrank.com/challenges/the-quickest-way-up/problem
Using BFS
Handle the constraint.
1. 100 cannot be the startpoint but the endpoint
2. If we have no solution, return -1
"""
from collections import deque


def quickestWayUp(ladders, snakes):
    ladders = {x:y for x, y in ladders}
    snakes = {x:y for x, y in snakes}
    path = {**ladders, **snakes}
    
    board = [-1] * 100
    board[0] = 0

    q = deque([1])
    while q:
        cur = q.popleft()
        
        for i in range(1, 7):            
            if cur+i <= 100 and board[cur+i-1] == -1:
                if cur+i in path:
                    board[path[cur+i]-1] = board[cur-1] + 1
                    q.append(path[cur+i])
                else:
                    q.append(cur+i)
                board[cur+i-1] = board[cur-1] + 1

    return board[99]
