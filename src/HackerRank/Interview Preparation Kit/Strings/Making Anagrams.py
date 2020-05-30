"""
https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
"""
#1. Using Hash
from collections import defaultdict

def makeAnagram(a, b):
    dic_a = defaultdict(int)
    dic_b = defaultdict(int)

    for c in a:
        dic_a[c] += 1
        
    for c in b:
        dic_b[c] += 1

    ans = 0
    for c in dic_a:
        if c in dic_b:
            ans += min(dic_a[c], dic_b[c])
            
    return len(a) + len(b) - 2 * ans
    
#2. Using Counter
from collections import Counter

def makeAnagram(a, b):
    a = Counter(a)
    b = Counter(b)
    
    c = a - b
    d = b - a
    e = c + d
    
    return len(list(e.elements()))
