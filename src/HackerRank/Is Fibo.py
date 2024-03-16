"""
https://www.hackerrank.com/challenges/is-fibo
Mathematical Problem
"""
#1. My Solution
def isFibo(n):
    first = 0
    second = 1
    temp = 0
    
    while temp < n:
        temp = first + second
        first = second
        second = temp
    
    if n == temp:
        return "IsFibo"
    return "IsNotFibo"
