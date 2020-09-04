"""
https://www.acmicpc.net/problem/8972
Implementation Problem
Check the position of break and if the whole loop breaks.
Counterexample
8 8
R......R
.R...RR.
..R..RR.
........
.....R..
......R.
....I...
.......R
1444544

Collect solution
>> kraj 5
Failed solution
>> kraj 5
>> kraj 7
"""
#1. My Solution
# R : mad aduino
# I : player
# . : blank
# I cannot escape the board 
# R moves to minimize abs(r1-r2) + abs(s1-s2)
# when R overlaps, it explodes
# I and R overlaps, game ends
from collections import defaultdict


def find(ry, rx, iy, ix):
    dist_min = float('inf')
    if ry - iy == 0:
        dy = 0
    elif ry - iy > 0:
        dy = -1
    else:
        dy = 1

    if rx - ix == 0:
        dx = 0
    elif rx - ix > 0:
        dx = -1
    else:
        dx = 1

    return dy, dx
    
    
r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
moves = [*map(int, input())]
d = [-1, 0, 1]
directions = [[(j, i) for i in d] for j in d[::-1]]
rs = defaultdict(int)

# Find I and R
for i in range(r):
    for j in range(c):
        if board[i][j] == 'I':
            iy, ix = i, j
        elif board[i][j] == 'R':
            rs[(i, j)] += 1

X = 0
flag = True
for m in moves:
    # Check flag is broken, if broken, ends the loop.
    if not flag:
        break
    
    X += 1
    i, j = divmod(m-1, 3)
    dy, dx = directions[i][j]
    
    #1. player moves
    if board[iy+dy][ix+dx] == 'R':
        print(f'kraj {X}')
        flag = False
        break
    else:
        board[iy][ix] = '.'
        iy += dy
        ix += dx
        board[iy][ix] = 'I'

    #2. R moves
    rs_temp = defaultdict(int)
    for ry, rx in rs:
        board[ry][rx] = '.'
        dy, dx = find(ry, rx, iy, ix)
        if board[ry+dy][rx+dx] == 'I':
            print(f'kraj {X}')
            flag = False
            break  # this breaks only inner loop
        else:
            rs_temp[(ry+dy, rx+dx)] += 1

    #3. R explodes
    rs_new = defaultdict(int)
    for r in rs_temp:
        if rs_temp[r] > 1:
            board[r[0]][r[1]] = '.'
        else:
            board[r[0]][r[1]] = 'R'
            rs_new[r] += 1
            
    rs = rs_new

    # print(iy, ix, rs)
    # [print(''.join(row)) for row in board]

if flag:            
    [print(''.join(row)) for row in board]
