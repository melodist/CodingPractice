"""
https://programmers.co.kr/learn/courses/30/lessons/17679
"""
def check(i, j, board):
    for dx, dy in [(0, 1), (1, 0), (1, 1)]:
        if board[i][j] != board[i+dx][j+dy]:
            return False
    return True


def delete(m, n, board):
    dels = set()
    for i in range(m-1):
        for j in range(n-1):
            if check(i, j, board) and board[i][j] != -1:
                dels.add((i, j))
                dels.add((i+1, j))            
                dels.add((i, j+1))            
                dels.add((i+1, j+1))

    for i, j in dels:
        board[i][j] = -1

    return len(dels)


def descend(i, j, board):
    cur = i
    while board[cur][j] == -1 and cur > 0:
        cur -= 1

    while cur < i:
        board[cur][j], board[cur+1][j] = board[cur+1][j], board[cur][j]
        cur += 1


def refresh(m, n, board):
    for i in range(m-1, 0, -1):
        for j in range(n):
            if board[i][j] == -1:
                descend(i, j, board)


def solution(m, n, board):
    board = [list(s) for s in board]

    answer = 0
    while True:
        temp = delete(m, n, board)
        if temp == 0:
            break
        answer += temp
        refresh(m, n, board)

    return answer
