"""
https://www.acmicpc.net/problem/17144
Implementation Problem
"""
#1. My Solution
import sys


input = sys.stdin.readline
r, c, t = map(int, input().strip().split())
s = []
a = [list(map(int, input().strip().split())) for _ in range(r)]

for i in range(r):
    if a[i][0] == -1:
        s.append(i)
        s.append(i+1)
        break

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(t):
    #1. Diffusion
    b = []    
    for i in range(r):
        r_next = []
        for j in range(c):
            if a[i][j] == -1:
                r_next.append(-1)
            else:
                temp = a[i][j]
                for di, dj in dirs:
                    if 0 <= i + di < r and 0 <= j + dj < c and a[i+di][j+dj] != -1:
                        temp += (a[i+di][j+dj] // 5) - (a[i][j] // 5)
                r_next.append(temp)
        b.append(r_next)

    a = list(map(list, b))
    
    #2. Circulation
    a[s[0]][2:] = b[s[0]][1:-1]
    a[s[0]][1] = 0

    for i in range(s[0]):
        a[i][-1] = b[i+1][-1]
        a[i+1][0] = b[i][0]
        
    a[0][:-1] = b[0][1:]
    a[s[0]][0] = -1
    
    a[s[1]][2:] = b[s[1]][1:-1]
    a[s[1]][1] = 0
    
    for i in range(s[1], r-1):
        a[i+1][-1] = b[i][-1]
        a[i][0] = b[i+1][0]
        
    a[-1][:-1] = b[-1][1:]
    a[s[1]][0] = -1
    
print(sum(map(sum, a)) + 2)

#2. Optimized Solution
# Optimization not using array deepcopy
import sys

R, C, T=map(int, input().split())
Map=[[0]*C for _ in range(R)]

Cleaner = list()

for i in range(R):
    Map[i][:] = list(map(int, sys.stdin.readline().split()))
    if Map[i][0] == -1:
        Cleaner.append([i,0])

# up right down left
#axis = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# save dust map before cleaning
def Spread():
    NewMap=[[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(2):
            tmp = 0
            if Map[i][j] > 4 :
                dust=Map[i][j]//5
                
                NewMap[i][j+1] +=dust
                tmp += 1
                if i + 1 < R and Map[i+1][j] != -1:
                    NewMap[i+1][j] += dust
                    tmp += 1
                if j -1 > -1 and Map[i][j-1] != -1:
                    NewMap[i][j-1] += dust
                    tmp += 1
                if i -1 > -1 and Map[i-1][j] != -1:
                    NewMap[i-1][j] += dust
                    tmp += 1
                NewMap[i][j]=NewMap[i][j]+Map[i][j]-tmp*dust
            else:
                NewMap[i][j]=NewMap[i][j]+Map[i][j]
        for j in range(2,C):
            tmp = 0
            if Map[i][j] > 4 :
                dust=Map[i][j]//5
                if j + 1 < C :
                    NewMap[i][j+1] +=dust
                    tmp += 1
                if i + 1 < R :
                    NewMap[i+1][j] += dust
                    tmp += 1
                    
                NewMap[i][j-1] += dust
                tmp += 1
                if i -1 > -1 :
                    NewMap[i-1][j] += dust
                    tmp += 1
                NewMap[i][j]=NewMap[i][j]+Map[i][j]-tmp*dust
            else:
                NewMap[i][j]=NewMap[i][j]+Map[i][j]
    return NewMap

def Cleaning():
    # Up cycle / Count clockwise
    tmpx = Cleaner[0][0]
    for i in range(tmpx):
        Map[tmpx-i][0] = Map[tmpx-i-1][0]
    for i in range(C-1):
        Map[0][i] = Map[0][i+1]
    for i in range(tmpx):
        Map[i][C-1]=Map[i+1][C-1]
    for i in range(C-1):
        Map[tmpx][C-1-i]=Map[tmpx][C-2-i]
    Map[tmpx][0] = -1
    Map[tmpx][1] = 0

    # Down cycle / clockwise
    tmpx = Cleaner[1][0]
    
    for i in range(R-tmpx-1):
        Map[tmpx+i][0] = Map[tmpx+i+1][0]
    for i in range(C-1):
        Map[R-1][i]=Map[R-1][i+1]
    for i in range(R-tmpx-1):
        Map[R-1-i][C-1] = Map[R-2-i][C-1]
    for i in range(C-1):
        Map[tmpx][C-1-i] = Map[tmpx][C-2-i]
    Map[tmpx][0] = -1
    Map[tmpx][1] = 0


for m in range(T):
    Map = Spread()
    Cleaning()

print(sum([sum(row) for row in Map])+2)
