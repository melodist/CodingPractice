"""
https://www.acmicpc.net/problem/1949
Tree dynamic programming using recursion
"""
#1. My Soltuion
import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)
n = int(input().strip())
graph = [[] for _ in range(n+1)]
peoples = [0] + [*map(int, input().strip().split())]
for _ in range(n-1):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False] * (n+1)

def find(r):
    c1=peoples[r]; c2 =0
    visited[r] = True
    for s in graph[r]:
        if not visited[s]:
            c11, c21 = find(s)
            c1 += c21
            c2 += max(c11, c21)
 
    return c1, c2
    
c1, c2 = find(1)
print(max(c1, c2))
