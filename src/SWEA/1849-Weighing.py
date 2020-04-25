"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LeQJqDpwDFAXc&categoryId=AV5LeQJqDpwDFAXc&categoryType=CODE
1. Disjoint-set 이용하여 무게 측정 여부 확인.
2. Union할 시 무게 측정하여 weigth에 기록함.
parent : 각 node의 부모를 기록. 
weight : weight[i] = root - i
rank : 각 node의 순서 기록. 가장 rank가 큰 node가 루트임.
"""
from collections import defaultdict


def find(a):
    if not parent[a]:
        return a
    pa = parent[a]
    parent[a] = find(pa)
    weight[a] += weight[pa]
    return parent[a]


def union(a, b, w):
    pa = find(a)
    pb = find(b)
    if pa == pb:
        return
    diff = weight[b] - weight[a]
    if rank[pa] > rank[pb]:
        pa, pb = pb, pa
        w = -w
        diff = -diff
    weight[pa] = w + diff
    parent[pa] = pb
    if rank[pa] == rank[pb]:
        rank[pb] += 1


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    parent = defaultdict(int)
    weight = defaultdict(int)
    rank = defaultdict(int)
    ans = []
    for _ in range(M):
        work = input()
        if work[0] == '!':
            a, b, w = map(int, work.split()[1:])
            union(a, b, w)
        else:
            a, b = map(int, work.split()[1:])
            if find(a) == find(b):
                # (root - a) - (root - b) == (b - a)
                ans.append(weight[a] - weight[b]) 
            else:
                ans.append('UNKNOWN')
                
    ret = ' '.join(map(str, ans))
    print(f'#{test_case} {ret}')
