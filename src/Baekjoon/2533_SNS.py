"""
https://www.acmicpc.net/problem/2533
Tree dynamic programming
Using DFS
"""
#1. My Solution
import sys


def solve(cur):
    check[cur] = False
    cache[cur][0] = 1  # Include this node
    cache[cur][1] = 0  # Exclude this node
    for child in graph[cur]:
        if check[child]:
            solve(child)
            cache[cur][0] += cache[child][1]
            cache[cur][1] += max(cache[child][0], cache[child][1])

sys.setrecursionlimit(1000000) 
n = int(input())
graph = [[] for _ in range(n+1)]
cache = [[0, 0] for _ in range(n+1)]
check = [True] * (n+1)

for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

solve(1)
print(n - max(cache[1][0], cache[1][1]))

#2. Other Solution
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
n=int(input())
adj=[[] for _ in range(n+1)]
for _ in range(n-1):
  u,v=map(int,input().split())
  adj[u].append(v)
  adj[v].append(u)
visit=[0]*(n+1)
def find_min(r):
  c1=1; c2=0  # c1 : r is early adapter
  visit[r]=1
  for s in adj[r]:
    if visit[s]==0:
      c11,c21=find_min(s)
      c1+=min(c11,c21)
      c2+=c11
  return c1,c2
c1,c2=find_min(1)
print(min(c1,c2))
