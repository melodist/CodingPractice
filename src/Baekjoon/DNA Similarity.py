"""
https://www.acmicpc.net/problem/2612
Using Dynamic Programming
"""
#1. My Solution (976ms)
n = int(input())
a = input()
m = int(input())
b = input()

dp = [[0] * (m+1) for _ in range(n+1)]
y_max = x_max = 0
value_max = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 3
        else:
            dp[i][j] = max(dp[i][j-1] - 2, dp[i-1][j] -2, dp[i-1][j-1] - 2, 0)
            
        if value_max < dp[i][j]:
            y_max, x_max = i, j
            value_max = dp[i][j]
            
print(value_max)
y = y_max
x = x_max
while dp[y][x] > 0:
    if dp[y][x-1] == dp[y][x] + 2:
        x -= 1
    elif dp[y-1][x] == dp[y][x] + 2:
        y -= 1
    else:
        x -= 1
        y -= 1
               
answer_a = a[y:y_max]
answer_b = b[x:x_max]

print(answer_a)
print(answer_b)
