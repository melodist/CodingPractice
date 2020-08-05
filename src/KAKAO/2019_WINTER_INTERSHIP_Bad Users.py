"""
https://programmers.co.kr/learn/courses/30/lessons/64064
set is unhashable, but frozenset is hashable
"""
#1. My Solution using regex, product, and frozenset
import re
from itertools import product


def solution(user_id, banned_id):
    bad = []
    
    for b in banned_id:
        b1 = b.replace("*", ".") + '$'
        temp = [u for u in user_id if re.match(b1, u)]
        bad.append(temp)

    answer = []
    for a in product(*bad):
        if len(set(a)) == len(banned_id):
            answer.append(frozenset(a))
        
    return len(set(answer))
    
#2. Other Solution not using frozenset
from itertools import product

def check(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] == "*":
            continue
        if str1[i] != str2[i]:
            return False
    return True

def solution(user_id, banned_id):
    answer = set()
    result = [[] for i in range(len(banned_id))]

    for i in range(len(banned_id)):
        for u in user_id:
            if check(banned_id[i], u):
                result[i].append(u)

    result = list(product(*result))
    for r in result:
        if len(set(r)) == len(banned_id):
            answer.add("".join(sorted(set(r))))

    return len(answer)
