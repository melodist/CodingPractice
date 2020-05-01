"""
https://www.acmicpc.net/problem/1543
Using Boyer-Moore-Horspool algorithm and greedy algorithm.
"""
import sys

T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()
n = len(T)
m = len(P)

bc = {key: m - P.rindex(key) - 1 for key in P[:-1]}
bc[P[-1]] = m

ans = 0
ind, j = m - 1, m - 1
while ind < n:
    if T[ind + j - m + 1] == P[j]:
        if j == 0:
            ans += 1
            ind += m
            j = m - 1
        else:
            j -= 1
    else:
        ind += bc.get(T[ind + j - m + 1], m) + j - m + 1
        j = m - 1

print(ans)
