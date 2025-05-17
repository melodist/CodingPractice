"""
https://www.hackerrank.com/challenges/ajourney
Combinatorics Problem
"""
#1. Simple Solution (Timeout)
def solve(n, k):
    return first(n,k) + last(n, k)
    
    
def first(n, k):
    ans = 0
    
    for i in range(n-1):
        ans += 1
        if ans >= math.log2(10**k):
            ans -= math.log2(10)

    return int(2**ans)
    
    
def last(n, k):
    ans = 1
    
    for i in range(n-1):
        ans *= 2
        if ans >= 10**k:
            ans %= 10**k
            
    return ans


#2. Using modulo operation
from decimal import Decimal


def solve(n, k):
    return first(n,k) + last(n, k)
    
    
def first(n, k):
    x = (n-1) * Decimal(2).log10()
    number_of_digits = int (math.ceil(x))
    return int(10 ** (x - number_of_digits + k))
    
    
def last(n, k):
    return power_by_mod(2, n-1, 10**k)
    
     
def power_by_mod (a, b, c):
    if b == 0:
        return 1
    a %= c
    if b == 1:
        return a
    t = power_by_mod(a, b // 2, c)
    t = (t * t) % c
    
    return t if b % 2 == 0 else (t * a) % c
