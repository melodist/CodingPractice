"""
https://www.acmicpc.net/problem/1094
"""
#1. Recursive
# n : number of rods, s : sum of rods, r : shortest rod
def cut(n, s, r):
    if s == X:
        return n
    else:
        r //= 2
        n += 1
        if s - r >= X:
            s -= r
            n -= 1
        return cut(n, s, r)

X = int(input())
print(cut(1, 64, 64))

#2. Bottom-up
# Rod should be divided by power of 2.
X = int(input())
cnt = 0
while X != 0:
    if X % 2 == 1:
        cnt += 1
    X //= 2
print(cnt)
