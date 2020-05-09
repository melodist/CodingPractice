"""
https://www.acmicpc.net/problem/18290
Using Dynamic Programming and Bit Mask.
"""
import sys

n, m, k = map(int, sys.stdin.readline().split())
INT_MIN = -1e18

arr = [0] * (n+1)
for i in range(1, n+1):
    c = sys.stdin.readline().rsplit()
    arr[i] = list(map(int, c))
    
mm = (1<<m) - 1
pre = [[0] * (mm+1) for i in range(n+1)]
bc = [0] * (mm+1)
for i in range(1, n+1):
    for j in range(mm+1):
        bc[j] = bin(j).count("1")
        for a in range(m):
            if j & (1<<a):
                pre[i][j] += arr[i][a]
                
dp = [[[0] * (mm+1) for _ in range(k+1)] for _ in range(n+1)]
for i in range(n+1):
    for j in range(k+1):
        for a in range(mm+1):
            dp[i][j][a] = INT_MIN
            if i == 0 and j == 0:
                dp[i][j][a] = 0
                
chk = [0] * (mm+1)
for i in range(mm+1):
    for j in range(1, m):
        if (i&(1<<j)) and (i&(1<<(j-1))):
            chk[i] = 1
            
            
for i in range(1, n+1):
    for a in range(mm+1):
        if chk[a]:
            continue
        for ba in range(mm+1):
            for j in range(bc[a], k+1):
                if a&ba == 0:
                    dp[i][j][a] = max(dp[i][j][a], dp[i-1][j-bc[a]][ba]+pre[i][a])
                    
ans = INT_MIN
for i in range(mm+1):
    ans = max(ans, dp[n][k][i])

print(ans)
