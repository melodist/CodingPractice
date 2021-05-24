"""
https://www.acmicpc.net/problem/11049
Using Dynamic Programming
"""
#1. Solution Using pypy3 (796ms)
n = int(input())
dp = [[-1] * n for _ in range(n)] # dp[i][j] = minimal calc count between i and j
m = []
for _ in range(n):
    r, c = map(int, input().split())
    m.append((r, c))
    

def func(x, y):
    if x == y:
        return 0
 
    ref = dp[x][y]
    if ref != -1:
        return ref
 
    mm = float('inf')
 
    for k in range(x, y):
        mm = min(mm, func(x, k) + func(k + 1, y) + m[x][0] * m[k][1] * m[y][1])
 
    dp[x][y] = mm
    return mm

print(func(0, n-1))
