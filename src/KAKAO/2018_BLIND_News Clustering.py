"""
https://programmers.co.kr/learn/courses/30/lessons/17677/
[^A-Za-z]+ means string include characters ^(not) A-Za-z
"""
#1. My solution
import re
from collections import Counter


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    p = re.compile('[a-z]{2}')

    s1 = [str1[i]+str1[i+1] for i in range(len(str1)-1)]
    s2 = [str2[i]+str2[i+1] for i in range(len(str2)-1)]

    m1 = [s for s in s1 if p.match(s)]
    m2 = [s for s in s2 if p.match(s)]

    c1 = Counter(m1)
    c2 = Counter(m2)

    c3 = c1 & c2
    c4 = c1 | c2

    ans = sum(c3.values()) / sum(c4.values()) if c3 != c4 else 1

    return int(ans*65536)
    
#2. Without Counter
import re


def solution(str1, str2):
    s1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if not re.findall('[^A-Za-z]+', str1[i:i+2])]
    s2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if not re.findall('[^A-Za-z]+', str2[i:i+2])]

    set1 = set(s1)
    set2 = set(s2)

    set3 = set1 & set2
    set4 = set1 | set2
    
    if len(set4) == 0:
      return 65536
      
    inter = sum([min(s1.count(i), s2.count(i)) for i in set3])
    union = sum([max(s1.count(i), s2.count(i)) for i in set4])

    return int(inter/union*65536)
