"""
https://school.programmers.co.kr/learn/courses/30/lessons/147355
Implementation Problem
"""
#1. My Solution
def solution(t, p):
    m = len(t)
    n = len(p)
    answer = 0
    for i in range(m-n+1):
        if int(t[i:i+n]) <= int(p):
            answer += 1
    return answer
