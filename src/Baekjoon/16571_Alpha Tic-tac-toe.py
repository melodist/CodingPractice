"""
https://www.acmicpc.net/problem/16571
Using backtracking
"""
#1. My Solution
def check():
    count = [0] * 8
    for i, r in enumerate(board):
        for v in r:
            if v == 1:
                count[i] += 1
            elif v == 2:
                count[i] -= 1

    for i, r in enumerate(zip(*board)):
        for v in r:
            if v == 1:
                count[i+3] += 1
            elif v == 2:
                count[i+3] -= 1
                
    for i in range(3):
        if board[i][i] == 1:
            count[6] += 1
        elif board[i][i] == 2:
            count[6] -= 1
            
        if board[i][2-i] == 1:
            count[7] += 1
        elif board[i][2-i] == 2:
            count[7] -= 1
            
    if count.count(3) > 0:
        return 'X'
    elif count.count(-3) > 0:
        return 'O'
    else:
        return 'D'
    
def backtrack(board, turn, player):
    if not turn:
        return check()
        
    opponent = 'O' if player == 'X' else 'X'
    
    empty = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                empty.append((i, j))
                
    moves = {}
    for i, j in empty:
        board[i][j] = 1 if player == 'X' else 2
        temp = check()
        if temp == 'D':
            moves[(i, j)] = backtrack(board, turn-1, opponent)
        else:
            moves[(i, j)] = temp
        board[i][j] = 0    
            
    results = set(moves.values())
    if player in results:
        return player
    elif 'D' in results:
        return 'D'
    else:
        return opponent
        
board = []
for _ in range(3):
    board.append([*map(int, input().split())])
    
turns = 0
for i in range(3):
    for j in range(3):
        if board[i][j] == 0:
            turns += 1

player = 'X' if turns % 2 == 1 else 'O'
winner = backtrack(board, turns, player)            
if player == winner: 
    print('W') 
elif winner == 'D':
    print(winner)
else:
    print('L')
    
#2. Other Solution
def winner(L, p):
    for i in range(0, 24, 3):
        a, b, c = L[row[i]], L[row[i+1]], L[row[i+2]]
        if a==b==c!=0: return a
    if 0 not in L: return -1
    
    reses = []
    for j in range(9):
        if L[j]: 
            continue
        L[j] = p
        reses.append(winner(L, 3-p))
        L[j] = 0

    if p in reses: 
        return p
    if -1 not in reses: 
        return 3-p

    return -1
    
    
X = lambda: list(map(int,input().split()))
L = X()+X()+X()
if sum(L) <= 1: print("D"); exit()
player = 1 if L.count(1) == L.count(2) else 2
row = [0,1,2, 3,4,5, 6,7,8, 0,3,6, 1,4,7, 2,5,8, 0,4,8, 2,4,6]

rp = (winner(L, player))
if rp == -1: 
    print("D")
else: 
    print("L" if rp != player else "W")
