"""
https://www.hackerrank.com/challenges/closest-number
Number Theory Problem
"""
#1. My Solution
def closestNumber(a, b, x): 
    k=a**b
    k=int(k)
    r=k%x

    if abs(x-r)<=r:
        return k+(x-r)
    elif k-r<1:
        return 0
    else:
        return k-r
