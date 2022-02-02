"""
https://programmers.co.kr/learn/courses/30/lessons/12985
"""
#1. Solution using math
import math


def solution(n,a,b):
    for i in range(int(math.log2(n))):
        if (a-1) // 2**i == (b-1) // 2**i:
            return i

    return int(math.log2(n))


#2. Solution using bit calculation
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()
