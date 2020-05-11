"""
https://programmers.co.kr/learn/courses/30/lessons/42839
set와 map을 이용하여 해결
| : 합집합(union)
- : 차집합(difference)
"""
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
