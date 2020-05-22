"""
https://www.acmicpc.net/problem/16197
Brute Force.
한 방향으로만 움직이므로 한 방향만 검사함.
"""
def check(c):
    return (0 > c[0] or n <= c[0]) or (0 > c[1] or m <= c[1])
    
def go(c, d):
    y, x = c
    dy, dx = d
    
    if dy == 0:
        if not (0 <= x + dx < m and board[y][x+dx] == 1):
            x += dx
    else:
        if not (0 <= y + dy < n and board[y+dy][x] == 1):
            y += dy
        
    return [y, x]
    
def generate(x, c1, c2):
    if x > 10:
        return 11
    
    if check(c1) ^ check(c2):
        return x
    
    if check(c1) and check(c2):
        return 11
        
    dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    
    ans = 11
    for d in dirs:
        c3 = go(c1, d)
        c4 = go(c2, d)
        ans = min(ans, generate(x+1, c3, c4))
        
    return ans

n, m = map(int, input().split())
board = [[0] * m for _ in range(n)]
coin = []

for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == '#':
            board[i][j] = 1
        else:
            if s[j] == 'o':
                coin.append([i, j])
            board[i][j] = 0
    
c1, c2 = coin
ans = generate(0, c1, c2)
print(ans if ans < 11 else -1)
