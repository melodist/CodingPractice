"""
https://school.programmers.co.kr/learn/courses/30/lessons/147355
Implementation Problem
"""
#1. Simple Solution
def solution(t, p):
    m = len(t)
    n = len(p)
    answer = 0
    for i in range(m-n+1):
        if int(t[i:i+n]) <= int(p):
            answer += 1
    return answer

#2. Pythonic Solution
def solution(t, p):
    return len([x for x in range(len(t)-len(p)+1) if int(t[x:x+len(p)]) <= int(p)])
