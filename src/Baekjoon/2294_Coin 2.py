"""
https://www.acmicpc.net/problem/2294
Using dynamic programming
"""
#1. My Solution (608ms)
import sys


input = sys.stdin.readline
n, k = map(int, input().split())
dp = [sys.maxsize] * (k+1)
dp[0] = 0
a = [int(input()) for _ in range(n)]

for i in range(n):
    for j in range(1, k+1):
        if j >= a[i]:
            dp[j] = min(dp[j-a[i]] + 1, dp[j])
    
print(dp[-1] if dp[-1] < sys.maxsize else -1)

#2. Other Solution (188ms)
def solution() :
    a, b = map(int, input().split())
    dp = [float('inf')] * 100001
    for i in range(a) :
        m = int(input())
        dp[m] = 1
        for j in range(m+1, b+1) :
            if dp[j] > dp[j-m] + 1 :
                dp[j] = dp[j-m] + 1
    if dp[b] == float('inf') : print(-1)
    else : print(dp[b])
solution()
