"""
https://school.programmers.co.kr/learn/courses/30/lessons/12935
Implementation Problem
"""
#1. My Solution
def solution(arr):
    if len(arr) == 1: return [-1]
    arr.remove(min(arr))
    return arr
