"""
https://programmers.co.kr/learn/courses/30/lessons/12905
Square could extend only left, up, and diagonal values are 1
"""
#1. My Solution
def solution(board):
    r = len(board)
    c = len(board[0])

    b = [[0] * (c+1)]
    for i, row in enumerate(board):
        b.append([0] + row)
        
    answer = 0
    for i in range(1, r+1):
        for j in range(1, c+1):
            b[i][j] = min(b[i-1][j], b[i][j-1], b[i-1][j-1]) + 1 if b[i][j] > 0 else 0
            answer = max(answer, b[i][j])
    
    return answer ** 2
