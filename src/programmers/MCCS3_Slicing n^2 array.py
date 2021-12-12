"""
https://programmers.co.kr/learn/courses/30/lessons/87390
Math Problem
"""
#1. My Solution
def solution(n, left, right):
    return [i//n + 1 if i//n > i%n else i%n + 1 for i in range(left, right+1)]
