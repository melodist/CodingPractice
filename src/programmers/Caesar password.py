"""
https://school.programmers.co.kr/learn/courses/30/lessons/12926
String Problem

ord(c) : Find ordinary position of character c
chr(i) : Find character matches with ascii code i
"""
#1. My Solution
def solution(s, n):
    answer = ''
    for c in s:
        if c.isupper():
            answer += chr(65 + (ord(c) + n - 65) % 26)
        elif c.islower():
            answer += chr(97 + (ord(c) + n - 97) % 26)
        else:
            answer += c
    return answer
