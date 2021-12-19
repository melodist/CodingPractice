"""
https://programmers.co.kr/learn/courses/30/lessons/12941
Math Problem
"""
#1. My Solution
def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer = 0
    for a, b in zip(A, B):
        answer += a * b
    return answer
