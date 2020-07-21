"""
"""
#1. My Solution - O(rows * cols) / O(moves)
def solution(board, moves):
    answer = 0
    n = len(board)
    m = len(board[0])
    board_stack = [[] for _ in range(m)]
    for j in range(m):
        for i in range(n-1, -1, -1):
            if board[i][j] != 0:
                board_stack[j].append(board[i][j])

    stack = []
    for m in moves:
        if board_stack[m-1]:
            temp = board_stack[m-1].pop()
            if temp != 0:
                if stack and temp == stack[-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(temp)

    return answer
    
#2. Other Solution - O(rows * moves)
def solution(board, moves):
    stacklist = [0]
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if stacklist[-1] != 0:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
