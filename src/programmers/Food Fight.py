"""
https://school.programmers.co.kr/learn/courses/30/lessons/134240
String Problem
"""
#1. My Solution
def solution(food):
    answer = ''
    for i, f in enumerate(food[1:]):
        answer += str(i+1) * (f // 2)
    return answer + "0" + answer[::-1]
