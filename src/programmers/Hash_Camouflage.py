"""
https://programmers.co.kr/learn/courses/30/lessons/42578?
Using Hash
"""
#1. My Solution
from collections import defaultdict
from functools import reduce


def solution(clothes):
    c = defaultdict(lambda:1)
    for v, k in clothes:
        c[k] += 1
        
    return reduce(lambda x, y: x*y, c.values()) - 1
    
#2. Other Solution
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1  # reduce(function, iterable, initializer=None)
    return answer
