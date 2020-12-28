"""
https://www.acmicpc.net/problem/1074
Using recursion
"""
#1. My Solution (84ms)
def solve(n, r, c):
    if r < 0 or c < 0:
        return 0
        
    if n == 1:
        return r * 2 + c
    
    x = 0
    if r >= 2**(n-1):
        x += 2
        r -= 2**(n-1)
    if c >= 2**(n-1):
        x += 1
        c -= 2**(n-1)
        
    return x * 2**(2*(n-1)) + solve(n-1, r, c)
    
n, r, c = map(int, input().split())
print(solve(n, r, c))
