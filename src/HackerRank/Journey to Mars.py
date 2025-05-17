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
