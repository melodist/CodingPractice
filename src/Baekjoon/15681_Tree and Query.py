"""
https://www.acmicpc.net/problem/15681
Tree Dynamic Programming
Using DFS
"""
#1. My Solution
import sys


def countsubtree(node):
    num_sub[node] = 1
    for child in graph[node]:
        if num_sub[child] == 0:
            countsubtree(child)
            num_sub[node] += num_sub[child]
        
    return num_sub[node]

    
sys.setrecursionlimit(1000000) 
n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
num_sub = [0] * (n+1)

for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

countsubtree(r)

ans = ''
for _ in range(q):
    ans += f'{num_sub[int(input())]}\n'
    
print(ans)
