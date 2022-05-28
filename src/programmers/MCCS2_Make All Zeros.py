"""
https://programmers.co.kr/learn/courses/30/lessons/76503
Using DFS and greedy algorithm
Make zero from the leaves
"""
#1. My Solution
from collections import deque 
import sys
sys.setrecursionlimit(3*10**5)

answer = 0
def solution(a, edges):
    def dfs(u):
        global answer
        
        for v in tree[u]:
            if not visited[v]:
                visited[v] = True
                temp = dfs(v)
                a[u] += temp

        answer += abs(a[u])
        
        return a[u]
    
    global answer
    if sum(a) != 0: return -1

    n = len(a)
    tree = [set() for _ in range(n)]
    visited = [False] * n
    visited[0] = True
    
    for u, v in edges:
        tree[u].add(v)
        tree[v].add(u)
    
    dfs(0)
    
    return answer

#2. Other Solution
import collections
def check(a):
    if sum(a)==0:
        return True
    return False

def solution(a, edges):
    tree = [[] for _ in range(len(a))]
    indegree = [0]*(len(a))
    for i,j in edges:
        tree[i].append(j)
        tree[j].append(i)
        indegree[i] += 1
        indegree[j] += 1

    leaf = collections.deque()
    for i in range(len(indegree)):
        if indegree[i]==1:
            leaf.append(i)
    visit = set()
    res = 0
    while leaf:
        now = leaf.popleft()
        visit.add(now)
        for nxt in tree[now]:
            if nxt not in visit:
                t = a[now]
                a[now] -= t
                a[nxt] += t
                res += abs(t)
                indegree[nxt] -= 1
                if indegree[nxt]==1:
                    leaf.append(nxt)
    if check(a):
        return res
    else:
        return -1
