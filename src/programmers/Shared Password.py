"""
https://school.programmers.co.kr/learn/courses/30/lessons/155652
Implementation Problem
"""
#1. My Solution
def solution(s, skip, index):
    chrs = [chr(i+97) for i in range(26)]
    for c in skip:
        chrs.remove(c)
    answer = ''
    
    for c in s:
        answer += chrs[(chrs.index(c) + index) % len(chrs)]
    return answer
