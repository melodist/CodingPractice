"""
https://programmers.co.kr/learn/courses/30/lessons/12973?language=python3
Implementation Problem
"""
#1. My Solution
def solution(s):
    stack = []
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
        
    return 0 if stack else 1
