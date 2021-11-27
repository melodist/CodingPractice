"""
https://programmers.co.kr/learn/courses/30/lessons/12981?language=python3
Implementation Problem
"""
#1. My Solution
def solution(n, words):
    visited = set()
    for i, w in enumerate(words):
        flag = True
        
        if w in visited:
            flag = False
            
        if i > 0 and words[i-1][-1] != w[0]:
            flag = False
            
        if len(w) == 1:
            flag = False
            
        if flag:
            visited.add(w)
        else:
            return [i % n + 1, i // n + 1]
        
    return [0, 0]
