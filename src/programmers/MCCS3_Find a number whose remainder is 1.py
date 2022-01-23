"""
https://programmers.co.kr/learn/courses/30/lessons/87389
Implementation Problem
"""
#1. Simple Solution
def solution(n):
    for i in range(2, n):
        if n % i == 1:
            return i
    return -1

#2. Optimal Solution
import math


def solution(n):
    x = n - 1
    for i in range(2, math.floor(math.sqrt(x)) + 1):
        if x % i == 0:
            return i
    return x
