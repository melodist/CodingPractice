"""
https://www.acmicpc.net/problem/14852
"""
#1. Solution Using Dynamic Programming (996ms)
n = int(input())

# dp(n) = 2*dp(n-1) + 3*dp(n-2) + 2*dp(n-3) + 2*(dp(n-4) + dp(n-3) + ... + dp(0))

dp = [1] * (n+1)
dp[1] = 2
dp[2] = 7
dp[3] = 22
MOD = 1000000007

s = 1
for i in range(4, n+1):
    dp[i] = (2*dp[i-1] + 3*dp[i-2] + 2*dp[i-3] + 2 * s) % MOD
    s += dp[i-3]
    
print(dp[n])

#2. Solution Using Bit Mask
# 0 : o 1 : o 2 : x
#     o     x     o
import sys

sys.setrecursionlimit(10**6)
n = int(input())

dp = [[0] * 3 for i in range(n+1)]
MOD = 1000000007
# n번째 열이 bit 상태일 경우 이를 채우는 경우의 수를 계산
def tiling(n, bit):
    if n < 0:
        return 0
    if n < 1:
        return 1 if bit == 0 else 0
    if dp[n][bit] > 0:
        return dp[n][bit]
    
    value = 0
    
    if bit == 0:
        value += 2 * tiling(n-1, 0)
        value += tiling(n-2, 0)
        value += tiling(n-1, 1)
        value += tiling(n-1, 2)
    elif bit == 1:
        value += tiling(n-1, 0)
        value += tiling(n-1, 2)
    else:
        value += tiling(n-1, 0)
        value += tiling(n-1, 1)
        
    dp[n][bit] = value % MOD
    return dp[n][bit]
    
print(tiling(n, 0))
