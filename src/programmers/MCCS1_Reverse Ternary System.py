"""
https://programmers.co.kr/learn/courses/30/lessons/68935
Implementation Problem
"""
#1. My Soltuion
def convert(n, base):
    ans = ''
    while n > 0:
        q, r = divmod(n, base)
        ans += str(r)
        n = q
    return ans[::-1]


def convert2(n):
    i = 0
    ans = 0
    while n > 0:
        q, r = divmod(n, 10)
        ans += r * (3**i)
        n = q
        i += 1
    return ans

def solution(n):
    s = convert(n, 3)
    return convert2(int(s[::-1]))
    
#2. Other Solution
def n_ary(n, base):
    result = []
    while n > 0:
        n, r = divmod(n, base)
        result.append(r)
    return ''.join(map(str, reversed(result)))

def solution(n):
    b3 = n_ary(n, 3)
    b3 = b3[::-1]
    return int(b3, 3)
