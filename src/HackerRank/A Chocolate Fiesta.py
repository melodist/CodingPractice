"""
https://www.hackerrank.com/challenges/a-chocolate-fiesta
Combinatorics Problem

If n_odd = 0, ans = 2**n - 1
If n_odd > 0, 
possible ways of choosing odd number from n_odd:
comb(n_odd, 1) + comb(n_odd, 3) + ... + comb(n_odd, n_odd) = 2**(n_odd - 1)
ans = 2**(n - n_odd) * 2**(n_odd-1)
"""
#1. My Solution
def solve(a):
    n = len(a)
    n_odd = len([x for x in a if x % 2 == 1])
    mod = 10**9 + 7

    return (pow(2, n - n_odd) * pow(2, n_odd - 1 if n_odd > 0 else 0) - 1) % mod

"""
If there is at least one odd element, let x be the last odd element. 
Choose a subset among the n-1 remaining values. 
If the sum is odd, then include x. Otherwise, don't include x. 
This way, the subset we choose always has an even sum. Thus the answer is 2^(n-1).
"""
#2. Other Solution
def solve(a):
    n_odd = len([x for x in a if x % 2 == 1])
    mod = 10**9+7
    return (pow(2, len(a)-1) - 1) % mod if n_odd > 0 else (pow(2, len(a)) - 1) % mod
