"""
https://www.hackerrank.com/challenges/between-two-sets/problem
Implementation Problem
Find Least Common Multiple (LCM) of A and Greates Common Divisor (GCD) of B
Using Euclidean Algorithm
"""
#1. My Solution
from functools import reduce


def getTotalX(a, b):
    def LCM(a, b):
        return (a * b) // GCD(a, b)

    def GCD(a, b):
        return b if a % b == 0 else GCD(b, a % b)

    lcm = reduce(LCM, a)
    gcd = reduce(GCD, b)

    answer = 0
    i = 1
    while lcm * i <= gcd:
        if gcd % (lcm * i) == 0:
            answer += 1
        i += 1
    
    return answer
    
#2 Solution using fraction library
from fractions import gcd



def getTotalX(a, b):
    def LCM(a, b):
        return (a*b)//gcd(a,b)

    lcm = reduce(LCM, a, 1)
    GCD = reduce(gcd, b)

    lcm_copy = lcm

    count = 0
    while lcm <= GCD:
        if(GCD % lcm) == 0:
            count += 1
        lcm += lcm_copy

    return count
