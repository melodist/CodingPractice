"""
https://school.programmers.co.kr/learn/courses/30/lessons/118666
Implementation Problem
"""
#1. My Solution
from collections import defaultdict

def solution(survey, choices):
    score = defaultdict(int)
    for (a, b), c in zip(survey, choices):
        score[a] += max(0, 4 - c)
        score[b] += max(0, c - 4)
            
    answer = [a if score[a] >= score[b] else b for a, b in ["RT", "CF", "JM", "AN"]]
    return ''.join(answer)
