"""
https://programmers.co.kr/learn/courses/30/lessons/12980?language=python3
Math problem
"""
#1. My Solution
def solution(n):
    ans = 0
    while n > 0:
        if n % 2 != 0:
            ans += 1
        n //= 2

    return ans
    
#2. Other Solution
def solution(n):
    return bin(n).count('1')
