"""
https://www.hackerrank.com/challenges/kundu-and-tree/problem
Using Disjoint Sets
"""
import operator as op
from functools import reduce


def comb(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


MOD = 10**9 + 7
n = int(input())
root = [0] * (n+1)
size = [1] * (n+1)

for i in range(n-1):
    a, b, c = input().split()
    if c == 'r':
        continue

    a, b = map(int, (a, b))
    if a > b:
        a, b = b, a

    while root[a] != 0:
        a = root[a]

    while root[b] != 0:
        b = root[b]
    
    if a == b:
        continue
    
    size[a] += size[b]
    size[b] = 0
    root[b] = a

ans = 0
for i in range(1, n):
    if not root[i] and size[i] > 1:
        ans += comb(size[i], 2) * (n - size[i])
        if size[i] > 2:
            ans += comb(size[i], 3)

print((comb(n, 3) - ans) % MOD)
