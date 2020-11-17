"""
https://www.acmicpc.net/problem/15961
Using sliding window
"""
#1. My Solution
import sys


input = sys.stdin.readline
n, d, k, c = map(int, input().strip().split())
sushi = [0] * n
for i in range(n):
    sushi[i] = int(input())

visited = [0] * (d+1)
temp = 0

for j in range(k):
    if visited[sushi[j]] == 0:
        temp += 1
    visited[sushi[j]] += 1
    
if visited[c] == 0:
    ans = temp + 1
else:
    ans = temp

i = k 
for i in range(1, n):
    if ans <= temp:
        ans = temp+1 if visited[c] == 0 else temp
    
    visited[sushi[i-1]] -= 1
    if visited[sushi[i-1]] == 0:
        temp -= 1
        
    if visited[sushi[(i+k-1) % n]] == 0:
        temp += 1
    visited[sushi[(i+k-1) % n]] += 1
    
print(ans)
