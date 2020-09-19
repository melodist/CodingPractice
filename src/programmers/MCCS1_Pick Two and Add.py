"""
https://programmers.co.kr/learn/courses/30/lessons/68644/
"""
#1. My Solution
from itertools import combinations


def solution(numbers):
    answer = set()
    for a, b in combinations(numbers, 2):
        answer.add(a+b)
    return sorted([*answer])

#2. Other Solution
def solution(numbers): return sorted({numbers[i] + numbers[j] for i in range(len(numbers)) for j in range(len(numbers)) if i>j})
