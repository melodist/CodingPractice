"""
https://www.acmicpc.net/problem/1647
Using Prim's Algorithm
Delete maximum cost from MST
"""
#1. My Solution (7792ms)
import sys
import heapq
from collections import defaultdict

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    if n == 2:
        return 0
        
    tree = defaultdict(list)
    visited = [False] * (n+1)
    hq = []
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        tree[a].append((b, c))
        tree[b].append((a, c))

    heapq.heappush(hq, (0, 1))
    ans = 0
    cmax = -1
    cnt = 0
    while cnt < n:
        c, u = heapq.heappop(hq)
        
        if visited[u]:
            continue
        visited[u] = True  
        cnt += 1

        if cmax < c: # Find maximum cost
            cmax = c
        ans += c
        
        for v, nc in tree[u]:
            heapq.heappush(hq, (nc, v))
                
    return ans - cmax
    
print(solve())
