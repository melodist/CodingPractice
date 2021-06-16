"""
https://www.acmicpc.net/problem/1535
Using Dynamic Programming
"""
#1. My Solution (72ms)
n = int(input())
L = [*map(int, input().split())]
J = [*map(int, input().split())]

prev = [0] * 100
next = [0] * 100
for i in range(n):
    for j in range(1, 100):
        if j >= L[i]:
            next[j] = max(next[j-1], prev[j], prev[j-L[i]]+J[i])
        else:
            next[j] = max(next[j-1], prev[j])
    
    prev = next[:]
    
print(prev[-1])
