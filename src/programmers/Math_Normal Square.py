"""
https://programmers.co.kr/learn/courses/30/lessons/62048
Find GCD (Greatest Common Divisior) using Euclidean Algorithm.

If A = aG, B = bG (a, b are coprime, and A > B)
Assume A = qB + r, aG = q*bG + r, so r = (a - qb) * G

Find (a - qb) and b ard coprime.
Assume a - qb = mp, b = np, a - q * np = np
-> a = (nq + m) p, b = np. But a and b are coprime. 
So (a - qb) and b are coprime.

So We can find GCD of A and B by finding GCD of r and B

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
