"""
https://www.hackerrank.com/challenges/triple-sum/problem
Using binary search and set
"""
#1. My Solution
import bisect


def triplets(a, b, c):
    a = sorted([*set(a)])
    b = set(b)
    c = sorted([*set(c)])
    return sum([bisect.bisect(a, x) * bisect.bisect(c, x) for x in b])
    
#2. Other Solution
def triplets(a, b, c):
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    
    ai = 0
    bi = 0
    ci = 0
    
    ans = 0
    
    while bi < len(b):
        while ai < len(a) and a[ai] <= b[bi]:
            ai += 1
        
        while ci < len(c) and c[ci] <= b[bi]:
            ci += 1
        
        ans += ai * ci
        bi += 1
    
    return ans
