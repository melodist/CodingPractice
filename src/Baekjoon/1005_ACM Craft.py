"""
https://www.acmicpc.net/problem/1005
Using topological sorting
"""
#1. My Solution(1632ms)
import sys
from collections import deque


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = [*map(int, input().split())]
    adj = [[] for _ in range(N+1)]
    ans = [0] * (N+1)
    indegree = [0] * (N+1)
    
    for _ in range(K):
        X, Y = map(int, input().split())
        adj[X].append(Y)
        indegree[Y] += 1
    
    q = deque([])    
    for i in range(1, N+1):
        if not indegree[i]:
            ans[i] = D[i-1]
            q.append(i)

    while q:
        u = q.popleft()
        
        for v in adj[u]:
            ans[v] = max(ans[v], ans[u]+D[v-1])
            indegree[v] -= 1
            
            if indegree[v] == 0:
                q.append(v)
                
    print(ans[int(input())])

#2. Other Solution(788ms)
import io
import os
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
sys.setrecursionlimit(10**6)


def solve():
    def dfs(u):
        if dp[u] != -1:
            return dp[u]
        m=max([dp[v] if dp[v]!=-1 else dfs(v) for v in adj[u]],default=0)
        dp[u]=m+t[u]
        return dp[u]

    n, k = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    dp = [-1 for _ in range(n+1)]
    t = [0]+list(map(int, input().split()))
    for _ in range(k):
        x, y = map(int, input().split())
        adj[y].append(x)
    w = int(input())
    print(dfs(w))


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
