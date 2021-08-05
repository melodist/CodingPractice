"""
https://programmers.co.kr/learn/courses/30/lessons/82612/
Math Problem
"""
#1. My Solution
def solution(price, money, count):  
    result = price * (count + 1) * count // 2
    return result - money if result > money else 0
