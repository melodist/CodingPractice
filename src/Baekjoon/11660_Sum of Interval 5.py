"""
https://www.acmicpc.net/problem/11660
Using Memoization
Sum of Interval should be calculated in O(1)
"""
#1. My Solution
import sys


n, m = map(int, input().split())

arr = [[*map(int, sys.stdin.readline().strip().split())] for _ in range(n)]

arr2 = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        arr2[i][j] = arr2[i-1][j] + arr2[i][j-1] + arr[i-1][j-1] - arr2[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())

    print(arr2[x2][y2] - arr2[x1-1][y2] - arr2[x2][y1-1] + arr2[x1-1][y1-1])
    
#2. Other Solution using accmulate()
import sys
from itertools import accumulate as acc

def sum_sq():
    for y in range(N):
        sq[y] = list(acc(sq[y]))
    for y in range(1, N):
        for x in range(N):
            sq[y][x] += sq[y-1][x]

def cal_sum(xys):
    y1, x1, y2, x2 = map(lambda x: x-1, xys)
    s = sq[y2][x2]
    if x1 != 0:
        s -= sq[y2][x1-1]
    if y1 != 0:
        s -= sq[y1-1][x2]
    if x1 != 0 and y1 != 0:
        s += sq[y1-1][x1-1]
    return s


input = sys.stdin.readline
N, M = map(int, input().split())
sq = []
for _ in range(N):
    sq.append(list(map(int, input().split())))

sum_sq()

for _ in range(M):
    print(cal_sum(map(int, input().split())))
