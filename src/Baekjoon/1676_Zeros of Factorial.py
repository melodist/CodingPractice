"""
https://www.acmicpc.net/problem/1676
Using mathmatics
"""
#1. My Solution (76ms)
def solve(n):
    ans = 0
    for i in range(1, n+1):
        if i % 5 == 0:
            while i % 5 == 0 and i > 1:
                i //= 5
                ans += 1
    
    return ans
    
print(solve(int(input())))

#2. Other Solution (52ms)
def cnt(n):
    c = 0
    for i in range(1,14):
        c += n // (5 ** i)
    return c

print(cnt(int(input())))
