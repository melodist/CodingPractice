"""
https://www.acmicpc.net/problem/15686
Implementation Problem
Using brute force
"""
#1. My Solution
import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().strip().split())
board = [[] for _ in range(n)]
for i in range(n):
    board[i] = [*map(int, input().strip().split())]

house = set()
chicken = set()

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.add((i, j))
        elif board[i][j] == 2:
            chicken.add((i, j))
            
k = len(house)
l = len(chicken)
hq = []
dist = [[0] * l for _ in range(k)]            
for i, a in enumerate(house):
    for j, b in enumerate(chicken):
        dist[i][j] = abs(a[0] - b[0]) + abs(a[1] - b[1])

answer = sys.maxsize
for p in combinations([*range(l)], m):
    temp = 0
    for i in range(k):
        temp += min([dist[i][x] for x in p])
        
    answer = min(answer, temp)
    
print(answer)

#2. Other Solution
import sys

input = sys.stdin.readline

n,m = list(map(int,input().strip().split()))
grid = []
for _ in range(n):
    grid.append(list(map(int,input().strip().split())))
house = []
chicken = []
for i in range(n):
    for j in range(n):
        v = grid[i][j]
        if v == 1:
            house.append([i,j])
        elif v == 2:
            chicken.append([i,j])
distance = []
for h in house:
    h_x,h_y = h
    h_l = []
    for c in chicken:
        c_x,c_y = c
        h_l.append(abs(h_x-c_x)+abs(h_y-c_y))
    distance.append(h_l)
distance = list(zip(*distance))
def check(select=[],index=-1):
    if len(select) == m:
        values = list(zip(*select))
        w = 0
        for v in values:
            w += min(v)
        return w
    if index == len(distance):
        return 999999
    #순서는 상관 없음
    ret = 99999999
    for i in range(index+1,len(distance)):
        select.append(distance[i])
        ret = min(ret,check(select,i))
        select.pop(-1)
    return ret
    
    
print(check())
