"""
https://school.programmers.co.kr/learn/courses/30/lessons/12948
String Problem
{m} means count of matching
?= means lookahead assertion
"""
#1. My Solution
import re


def solution(phone_number):
    return re.sub('\d', '*', phone_number[:-4]) + phone_number[-4:]

#2. Other Solution
import re

def hide_numbers(s):
    p = re.compile(r'\d(?=\d{4})')
    return p.sub("*", s, count = 0)
