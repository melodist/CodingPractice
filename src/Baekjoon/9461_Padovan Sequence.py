"""
https://www.acmicpc.net/problem/9461
Using dynamic programming
"""
#1. My Solution (84ms)
def solve(n):
    p = [0] * (n + 1)
    if n == 1 or n == 2 or n == 3:
        return 1
    elif n == 4 or n == 5:
        return 2
        
    p[1] = p[2] = p[3] = 1
    p[4] = p[5] = 2
    for i in range(6, n+1):
        p[i] = p[i-1] + p[i-5]
        
    return p[n]

for _ in range(int(input())):
    print(solve(int(input())))
    
#2. Other Solution (52ms)
from sys import stdin

P = [0, 1, 1, 1, 2, 2, 3]
for n in range(7, 101):
    P.append(P[n-1] + P[n-5])

next(stdin)
for n in map(int, stdin):
    print(P[n])
