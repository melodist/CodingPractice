"""
https://www.acmicpc.net/problem/7579
Using Dynamic Programming
"""
#1. My Solution (340ms)
n, m = map(int, input().split())
app = [*map(int, input().split())]
cancel = [*map(int, input().split())]
sum_cancel = sum(cancel)

dp = [0] * (sum_cancel+1) 

# app 합이 m 이하가 되도록 앱을 비활성화
# 비활성화 비용에 대한 최대 메모리 소비량을 구함
for i in range(n):
    for c in range(sum_cancel, cancel[i]-1, -1):
        dp[c] = max(dp[c], dp[c-cancel[i]] + app[i])
        
for i in range(sum_cancel+1):
    if dp[i] >= m:
        print(i)
        break
        
#2. Other Solution (108ms)
a, b = map(int, input().split())
l = list(zip(map(int, input().split()), map(int, input().split())))
l.sort(key=lambda t: t[1] / t[0])
dp = [0]
for m, c in l:
    dp = list(map(max, dp + [dp[-1]] * c, [0] * c + list(map(lambda v: v + m, dp))))
for i in range(len(dp) + 1):
    if dp[i] >= b:
        print(i)
        break
