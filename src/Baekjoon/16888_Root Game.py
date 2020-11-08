"""
https://www.acmicpc.net/problem/16888
Using dynamic programming and game theory
n = 2 : cubelover wins
n = i*i : koosaga wins
n = i + j*j, if dp[i] = 0 : koosaga wins
"""
#1. My Solution
import sys


input = sys.stdin.readline
MAX = 1000000

# dp[n] = 0 : cubelover wins / 1 : koosaga wins
dp = [0] * (MAX+1)
dp[1] = 1
dp[2] = 0

for i in range(1, int(MAX**0.5)+1):
    dp[i*i] = 1

for i in range(2, MAX+1):
    if dp[i] == 0:
        j = 1
        while i + j * j < MAX:
            dp[i + j * j] = 1
            j += 1
            
for _ in range(int(input().strip())):
    n = int(input().strip())
    
    if dp[n]:
        print("koosaga")
    else:
        print("cubelover")
