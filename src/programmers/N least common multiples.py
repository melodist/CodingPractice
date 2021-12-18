"""
https://programmers.co.kr/learn/courses/30/lessons/12953
Math Problem
"""
#1. My Solution
def solution(arr):
    # can replace with math.gcd(a, b)
    def gcd(a, b):
        while a!=0 and b!=0:
            if a > b:
                a = a % b
            else:
                b = b % a 
        return a + b
    
    answer = arr[0]
    
    for b in arr[1:]:
        g = gcd(answer, b)
        answer = answer * b // g

    return answer
