"""
https://www.acmicpc.net/problem/1405
Using DFS
"""
#1. My Solution (4132ms)
import sys


sys.setrecursionlimit(10**6)
N, e, w, s, n = map(int, input().split())
probs = [e/100, w/100, s/100, n/100]

visited = [[False] * (2*N+1) for _ in range(2*N+1)]
def check(y, x):
    return 0 <= y+N < 2*N+1 and 0 <= x+N < 2*N+1 and not visited[y+N][x+N]
    
def dfs(y, x, cnt, p):
    if cnt == N:
        return p
        
    visited[y+N][x+N] = True
    
    ans = 0 
    for i, (dy, dx) in enumerate([(1, 0), (-1, 0), (0, -1), (0, 1)]):
        if check(y+dy, x+dx):
            ans += dfs(y+dy, x+dx, cnt+1, p*probs[i])
            
    visited[y+N][x+N] = False

    return ans
    
print(dfs(0, 0, 0, 1))
