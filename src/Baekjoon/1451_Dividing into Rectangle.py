"""
https://www.acmicpc.net/problem/1451
Using prefix sum algorithm
"""
#1. My Solution
from itertools import accumulate


def cal_val(i, j):
    a = cum[i][j]
    b = cum[i][-1] - a
    c = cum[-1][j] - a
    d = cum[-1][-1] - (a + b + c)

    return max(a * b * (c+d), (a+b) * c * d, (a+c) * b * d, a * c * (b+d))
    
def cal_row(i):
    ans = 0
    for j in range(i+1, n):
        a = cum[i][-1]
        b = cum[j][-1] - a
        c = cum[-1][-1] - (a + b)
        ans = max(a * b * c, ans)
        
    return ans
    
def cal_col(i):
    ans = 0
    for j in range(i+1, m):
        a = cum[-1][i]
        b = cum[-1][j] - a
        c = cum[-1][-1] - (a + b)
        ans = max(a * b * c, ans)
        
    return ans

n, m = map(int, input().split())
arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = [int(c) for c in input().strip()]
    
cum = [[0] * (m) for _ in range(n)]
for i in range(n):
    cum[i] = [*accumulate(arr[i])]
for i in range(1, n):
    for j in range(m):
        cum[i][j] += cum[i-1][j]

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(cal_val(i, j), ans)

for i in range(n):
    ans = max(cal_row(i), ans)
    
for i in range(m):
    ans = max(cal_col(i), ans)
        
print(ans)
