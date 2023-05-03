"""
https://school.programmers.co.kr/learn/courses/30/lessons/161989
Implementation Problem
"""
#1. My Solution
def solution(n, m, section):
    right = 0
    answer = 0
    for i in section:
        if right < i:
            answer += 1
            right = i + m - 1

    return answer
