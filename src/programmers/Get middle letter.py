"""
https://programmers.co.kr/learn/courses/30/lessons/12903
String problem
"""
#1. My Solution
def solution(s):
    return s[(len(s)-1) // 2: len(s) // 2 + 1]
