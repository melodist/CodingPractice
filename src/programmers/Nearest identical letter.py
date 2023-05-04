"""
https://school.programmers.co.kr/learn/courses/30/lessons/142086
Using dictionary
"""
#1. My Solution
def solution(s):
    answer = []
    cache = {}
    for i, c in enumerate(s):
        if c in cache:
            answer.append(i - cache[c])
        else:
            answer.append(-1)
            
        cache[c] = i
            
    return answer
