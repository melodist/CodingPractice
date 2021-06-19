"""
https://www.acmicpc.net/problem/2623
Using topological sort
"""
#1. My Solution (68ms)
import sys


input = sys.stdin.readline
n, m = map(int, input().split())
tree = [[] for _ in range(n+1)]
deg = [0] * (n+1)
for _ in range(m):
    seq = [*map(int, input().split())]
    for i in range(1, seq[0]):
        tree[seq[i]].append(seq[i+1])
        deg[seq[i+1]] += 1

q = []    
for i in range(1, n+1):
    if deg[i] == 0:
        q.append(i)

ans = []
while q:
    u = q.pop()
    ans.append(str(u))
    
    for v in tree[u]:
        deg[v] -= 1
        if deg[v] == 0:
            q.append(v)

print('\n'.join(ans) if len(ans) == n else 0)
