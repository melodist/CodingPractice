"""
https://programmers.co.kr/learn/courses/30/lessons/70129
Implementation Problem
"""
#1. My Solution
def solution(s):
    def solve(s, count, zeros):
        if s == '1':
            return count, zeros

        t_zeros = s.count('0')
        t_ones = s.count('1')
        return solve(format(t_ones, 'b'), count+1, t_zeros+zeros)

    return solve(s, 0, 0)
    
#2. Other Solution
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]
