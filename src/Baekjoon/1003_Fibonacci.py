"""
https://www.acmicpc.net/problem/1003
Using dynamic programming
"""
#1. Solution using dynamic programming (76ms)
import sys


input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    
    if n == 0:
        print(1, 0)
        continue
    elif n == 1:
        print(0, 1)
        continue
    
    zeros = [0] * (n+1)
    ones = [0] * (n+1)
    zeros[0] = 1
    ones[1] = 1
    
    for i in range(2, n+1):
        zeros[i] = zeros[i-1] + zeros[i-2]
        ones[i] = ones[i-1] + ones[i-2]
        
    print(zeros[n], ones[n])

#2. Other Solution (52ms)
import sys
T = int(input())
dp = [[1,0], [0,1]]
q = [int(sys.stdin.readline()) for _ in range(T)]

for i in range(2,max(q)+1):
    dp.append([dp[i-2][0]+dp[i-1][0], dp[i-2][1]+dp[i-1][1]])
for i in q:
    print(dp[i][0], dp[i][1])
    
