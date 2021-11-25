"""
https://programmers.co.kr/learn/courses/30/lessons/70128?language=python3
Implementation Problem
"""
#1. My Solution
def solution(a, b):
    return sum([x * y for x, y in zip(a, b)])
