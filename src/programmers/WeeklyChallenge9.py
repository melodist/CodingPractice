"""
https://programmers.co.kr/learn/courses/30/lessons/86971
Using BFS
"""
#1. My Solution using BFS
from collections import deque


def solution(n, wires):
    def bfs(u, v):
        visited = [False] * (n+1)
        visited[u] = True
        q = deque([u])
        count = 0
        while q:
            curr = q.popleft()
            count += 1
            for a in tree[curr]:
                if not visited[a] and a != v:
                    visited[a] = True
                    q.append(a)

        return count
    
    tree = [[] for _ in range(n+1)]
    for u, v in wires:
        tree[u].append(v)
        tree[v].append(u)
        
    answer = float('inf')
    for u, v in wires:
        answer = min(abs(n - 2 * bfs(u, v)), answer)
        
    return answer

#2. Solution Using Union-Find
uf = []

def find(a):
    global uf
    if uf[a] < 0: return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    if pa == pb: return
    uf[pa] += uf[pb]  # (-1) + (-1)
    uf[pb] = pa

def solution(n, wires):
    global uf
    answer = int(1e9)
    k = len(wires)
    for i in range(k):
        uf = [-1 for _ in range(n+1)]
        tmp = [wires[x] for x in range(k) if x != i]
        for a, b in tmp: merge(a, b)  # Merge Two Tree which node is connected
        v = [x for x in uf[1:] if x < 0]
        answer = min(answer, abs(v[0]-v[1]))

    return answer
