"""
https://programmers.co.kr/learn/courses/30/lessons/62048
Using GCD
If w and h are coprime, Diagonal passes (w-1) lines and (h-1) lines.
So total broken square will be 1 + (w-1) + (h-1) = w + h - 1.
If w and h has GCD, it will be w + h - gcd(w, h)
"""
def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


def solution(w, h):
    whole = w * h;
    broken = w + h - gcd(w, h)
    return whole - broken
