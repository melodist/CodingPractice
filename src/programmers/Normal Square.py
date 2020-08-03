"""
https://programmers.co.kr/learn/courses/30/lessons/62048
Using GCD
"""
def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


def solution(w, h):
    whole = w * h;
    broken = w + h - gcd(w, h)
    return whole - broken
