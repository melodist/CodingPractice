"""
https://programmers.co.kr/learn/courses/30/lessons/12938?language=python3
Using mathematics
"""
#1. My Solution
def solution(n, s):
    if n > s:
        return [-1]
    answer = [s // n] * n
    for i in range(s % n):
        answer[n-1-i] += 1
    return answer
