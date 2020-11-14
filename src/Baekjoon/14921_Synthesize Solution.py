"""
https://www.acmicpc.net/problem/14921
Using two pointer approach
"""
#1. My Solution
import sys

input = sys.stdin.readline
n = int(input().strip())
arr = [*map(int, input().strip().split())]

i = 0
j = n-1
ans = sys.maxsize
while True:
    if i == j:
        break
    
    temp = arr[i] + arr[j]
    if abs(temp) < abs(ans):
        ans = temp
        
    if temp > 0:
        j -= 1
    elif temp < 0:
        i += 1
    else:
        break
    
print(ans)
