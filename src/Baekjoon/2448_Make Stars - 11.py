"""
https://www.acmicpc.net/problem/2448
Using recursion
"""
#1. My Solution (912ms)
import math


def triangle(i, j):
    points = [(i, j), (i+1, j-1), (i+1, j+1),
        (i+2, j-2), (i+2, j-1), (i+2, j), (i+2, j+1), (i+2, j+2)]
        
    for y, x in points:
        board[y][x] = '*'

def solve(u, v, k):
    if k == 0:
        triangle(u, v)
        return
        
    r = 2**k
    c = 6*r - 1
    
    dv = c // 4
    du = 3*(2**(k-1))
    
    solve(u, v, k-1)
    solve(u + du, v + dv + 1, k-1)
    solve(u + du, v - dv - 1, k-1)

n = int(input())
r = n // 3
k = int(math.log2(r))
c = 6 * r - 1

board = [[' ']* c for _ in range(n)]
solve(0, c//2, k)

[print(''.join(r)) for r in board]

#2. Other Solution (104ms)
def draw_next(lines, shift):
    for i in range(len(lines)):
        lines.append(lines[i]+' '+lines[i])
    for i in range(shift):
        lines[i] = ' '*shift + lines[i] + ' '*shift

def draw_lines(lines):
    print('\n'.join(lines))

def draw_triangle(height):
    lines = ['  *  ',
             ' * * ',
             '*****']

    i = 0
    while height > 3:
        draw_next(lines, 3*(2**i))
        height /= 2
        i+=1

    draw_lines(lines)
    
draw_triangle(int(input()))
