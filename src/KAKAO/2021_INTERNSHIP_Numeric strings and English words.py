"""
https://programmers.co.kr/learn/courses/30/lessons/81301
String Problem
"""
#1. My Solution
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four'
            ,'five', 'six', 'seven', 'eight', 'nine']
    for i, w in enumerate(words):
        s = s.replace(w, str(i))
    return int(s)
