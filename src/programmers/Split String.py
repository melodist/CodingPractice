"""
https://school.programmers.co.kr/learn/courses/30/lessons/140108
String Problem
"""
#1. My Solution
def solution(s):
    answer = 0
    cnt_first = 0
    cnt_others = 0
    
    for c in s:
        if cnt_first == cnt_others:
            answer += 1
            first = c
            
        if c == first: 
            cnt_first += 1
        else:
            cnt_others += 1
            
    return answer
