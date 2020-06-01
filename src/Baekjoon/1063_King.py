"""
https://www.acmicpc.net/problem/1063
"""
k, s, n = input().split()
board = [[0] * 8 for _ in range(8)]
king = (int(k[1])-1 , ord(k[0]) - ord('A'))
stone = (int(s[1])-1, ord(s[0]) - ord('A'))
moves = {'R':(0, 1), 'L':(0, -1), 'B':(-1, 0), 'T':(1, 0),
    'RT':(1, 1), 'LT':(1, -1), 'RB':(-1, 1), 'LB':(-1, -1)
}

def check(xx, yy):
    return True if 0 <= xx < 8 and 0<= yy < 8 else False
        
for i in range(int(n)):
    dy, dx = moves[input().strip()]
    ky, kx = king
    
    #1. Move King
    if not check(ky+dy, kx+dx):
        continue
        
    #2. Move stone
    if stone == (ky+dy, kx+dx):
        sy, sx = stone
        if not check(sy+dy, sx+dx):
            continue
        stone = (sy+dy, sx+dx)
        
    king = (ky+dy, kx+dx)
    
print(chr(ord('A') + king[1]) + str(king[0]+1))
print(chr(ord('A') + stone[1]) + str(stone[0]+1))
