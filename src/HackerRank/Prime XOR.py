"""
Using dynamic programming
"""
#1. My Solution
from collections import Counter


def is_prime(n):
    i = 2
    if n < i: return False
    while i*i <= n:
        if n % i == 0: return False
        i += 1
    return True


def primeXor(a):
    MOD = 10**9 + 7
    count = 0
    c = Counter(a)
    M = 8192
        
    dp = [0] * M
    dp[0] = 1 # XOR value for any empty set is 1
    range_M = range(M)

    for e in c.keys():
        even, odd = (c[e]//2 + 1), ((c[e] + 1)//2)
        dp = [(dp[i] * even + dp[i^e] * odd) % MOD for i in range_M]

    cache = {}
    for j in range_M:
        if j not in cache:
            cache[j] = is_prime(j)
        if cache[j]:
            count += dp[j]
            if count > MOD:
                count %= MOD

    return count
