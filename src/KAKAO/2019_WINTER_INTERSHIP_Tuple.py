"""
https://programmers.co.kr/learn/courses/30/lessons/64065
"""
#1. My solution
from collections import defaultdict

def solution(s):
    dic = defaultdict(int)
    temp = ""
    for c in s:
        if c.isdigit():
            temp += c
        else:
            if temp:
                dic[int(temp)] += 1
            temp = ""

    dic_sorted = sorted(dic.items(), key = lambda x: x[1], reverse=True)
    return [int(key) for key, val in dic_sorted]
    
#2. Optimal Solution
from collections import Counter
import re

def solution(s):
    p = re.findall('\d+', s)
    return [int(key) for key, val in sorted(Counter(p).items(), key=lambda x:x[1], reverse=True)]
