"""
https://school.programmers.co.kr/learn/courses/30/lessons/132267
Mathematical Problem
"""
#1. My Solution
def solution(a, b, n):
    answer = 0
    while n >= a:
        q, r = divmod(n, a)
        answer += b * q
        n = b * q + r

    return answer

#2. Other Solution
solution = lambda a, b, n: max(n - b, 0) // (a - b) * b
