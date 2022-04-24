"""
https://programmers.co.kr/learn/courses/30/lessons/12915
Using comparator
"""
#1. My Solution
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))
