"""
https://programmers.co.kr/learn/courses/30/lessons/12924
Math Problem
"""
#1. My Solution
def solution(n):
    answer = 0
    left = 0
    right = 1
    curr = 1
    
    while left < right:
        if curr >= n:
            answer += 1
            left += 1
            curr -= left
        elif curr > n:
            left += 1
            curr -= left
        else:
            right += 1
            curr += right
    return answer
