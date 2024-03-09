"""
https://www.hackerrank.com/challenges/russian-peasant-exponentiation
Mathematical Problem
"""
#1. My Solution
def mul(a, b, c, d, m):
    x = a * c - b * d
    y = a * d + b * c
    x = (m + x % m) % m
    y = (m + y % m) % m
    return (x, y)

def solve(a, b, k, m):
    if k == 0:
        return (1, 0)
    u, v = solve(a, b, k // 2, m)
    u, v = mul(u, v, u, v, m)
    if k % 2:
        u, v = mul(u, v, a, b, m)
    return (u, v)
