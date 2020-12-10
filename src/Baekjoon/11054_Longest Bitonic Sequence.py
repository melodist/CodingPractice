"""
https://www.acmicpc.net/problem/11054
Longest Increasing Sequence (LIS) Problem
Using dynamic programming
"""
#1. My Solution (436ms)
import sys


input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
dp = [[1] * n for _ in range(2)]  # dp[0][i] means length of LIS ends at i
dp[0][0] = dp[1][0] = 1

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j] and dp[0][i] < dp[0][j] + 1:  # all value in LIS at j is smaller than a[i]
            dp[0][i] += 1
        if a[n-1-i] > a[n-1-j] and dp[1][n-1-i] < dp[1][n-1-j] + 1:
            dp[1][n-1-i] += 1            

ans = 0
for a, b in zip(dp[0], dp[1]):
    ans = max(a+b-1, ans)
    
print(ans)

#2. Other Solution using binary search (60ms)
import sys
import bisect

def l(a,n,p):
    v=[-1]
    a=a[::p]
    d=[0]*n
    for i in range(n):
        if v[-1]<a[i]: 
            v+=[a[i]]
            d[i]=len(v)-1
        else: 
            v[bisect.bisect_left(v,a[i])]=a[i]
            d[i]=d[i-1]
    return d[::p]

n=int(input())
a=[*map(int,input().split())]
d=list(map(lambda x,y:x+y-1, l(a,n,1),l(a,n,-1)))
print(max(d))
