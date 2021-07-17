"""
https://www.acmicpc.net/problem/1298
Using Biparite Matching
"""
#1. My Solution (80ms)
import sys


def dfs(u):
    for v in arr[u]:
        if not visited[v]:
            visited[v] = True
            
            if matched[v] == 0 or dfs(matched[v]):
                matched[v] = u
                return True
            
    return False
    

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
arr = [[] for i in range(n+1)]
matched = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)

ans = 0
for i in range(1, n+1):
    visited = [False] * (n+1)
    if (dfs(i)):
        ans += 1

print(ans)
