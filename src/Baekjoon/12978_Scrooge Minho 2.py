"""
https://www.acmicpc.net/problem/12978
Tree dynamic programming
"""
#1. My Soltuion
import sys


def dfs(curr, parent):
    for child in graph[curr]:
        if child == parent:
            continue
        dfs(child, curr)
        dp0[curr] += min(dp0[child], dp1[child])  # dp0[curr] should include minimum value
        dp1[curr] += dp0[child]  # dp1[curr] should include all dp0[child]
    
    dp0[curr] += 1

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
graph = [set() for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)
    
dp0 = [0] * 100001  # dp0[v] for including v
dp1 = [0] * 100001  # dp1[v] for not including v

dfs(1, 0)
print(min(dp0[1], dp1[1]))
