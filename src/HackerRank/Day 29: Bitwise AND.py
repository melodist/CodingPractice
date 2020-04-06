"""
https://www.hackerrank.com/challenges/30-bitwise-and/problem
K보다 작은 target에 대하여
x = target | 2**n 이면서 x != target인 값이 S에 존재하는지 확인
"""
def find_target(s, k, n):
    target = k-1
    while target > 0:
        digit = 1
        temp = target | digit
        while temp <= n:
            if temp in s and temp != target:
                return target
            digit *= 2
            temp = target | digit
            
        target -= 1
    
    return target
