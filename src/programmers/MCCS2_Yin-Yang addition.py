"""
https://programmers.co.kr/learn/courses/30/lessons/76501
Implementation Problem
"""
#1. My Solution
def solution(absolutes, signs):
    return sum([a if s else -a for a, s in zip(absolutes, signs)])
