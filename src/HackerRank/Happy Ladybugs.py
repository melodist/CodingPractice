"""
https://www.hackerrank.com/challenges/happy-ladybugs/problem
Implementation Problem
"""
#1. My Solution
from collections import defaultdict


def happyLadybugs(b):
    cnt = defaultdict(int)
    for c in b:
        cnt[c] += 1
        
    if '_' in cnt:
        for k in cnt:
            if k == '_':
                continue
            elif cnt[k] == 1:
                return 'NO'
    else:
        prev = b[0]
        count = [1]
        for c in b[1:]:
            if prev == c:
                count[-1] += 1
            else:
                count.append(1)
                prev = c
                
        for i in count:
            if i < 2:
                return 'NO'
    
    return 'YES'
