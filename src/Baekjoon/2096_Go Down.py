"""
https://www.acmicpc.net/problem/2096
Using Dynamic Programming and Sliding Window
"""
n = int(input())
dp_max = list(map(int, input().split()))
dp_min = dp_max.copy()

for i in range(n-1):
    a, b, c = map(int, input().split())
    temp = [0] * 3
    # Using Sliding Window
    temp[0] = max(dp_max[0:2]) + a
    temp[1] = max(dp_max) + b
    temp[2] = max(dp_max[1:]) + c
    
    # Memoization
    dp_max[:] = temp[:]
    
    temp = [0] * 3
    temp[0] = min(dp_min[0:2]) + a
    temp[1] = min(dp_min) + b
    temp[2] = min(dp_min[1:]) + c
    
    dp_min[:] = temp[:]
    
print(max(dp_max), min(dp_min))
