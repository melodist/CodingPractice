"""
https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
Read the conditions precisely
"""
from collections import Counter

def isValid(s):
    a = Counter(s)
    b = Counter(a.values())
    c = list(b.keys())
    if len(c) > 2:
        return 'NO'
    elif len(c) == 1:
        return 'YES'
    else:       
        d = list(b.values())
        if d[0] == 1:
            return 'YES' if c[0] - c[1] == 1 or c[0] == 1 else 'NO'
        elif d[1] == 1:
            return 'YES' if c[1] - c[0] == 1 or c[1] == 1 else 'NO'
        else:
            return 'NO'
