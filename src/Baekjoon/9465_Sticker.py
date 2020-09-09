"""
https://www.acmicpc.net/problem/9465
Using Dynamic Programming
"""
#1. My Solution
import sys

for _ in range(int(input())):
    n = int(input())
    arr = [[*map(int, sys.stdin.readline().strip().split())], [*map(int, sys.stdin.readline().strip().split())] ]

    if n == 1:
        print(max(arr[0][0], arr[1][0]))
        continue
        
    dp = [[0] * n, [0] * n]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[0][1] = dp[1][0] + arr[0][1]
    dp[1][1] = dp[0][0] + arr[1][1]
    for i in range(2, n):
        for j in range(2):
            dp[j][i] = max(dp[j-1][i-1], dp[j-1][i-2]) + arr[j][i]
            
    print(max(dp[0][-1], dp[1][-1]))

#2. Other Solution
from sys import stdin
read = lambda: stdin.readline().rstrip()
for _ in range(int(read())):
    n = int(read())
    a, b = 0, 0
    c, d = 0, 0
    arr1 = tuple(map(int, read().split()))
    arr2 = tuple(map(int, read().split()))
    for i in range(n):
        a, b, c, d = b, max(c, d) + arr1[i], d, max(a, b) + arr2[i]
    print(max(b, d))
