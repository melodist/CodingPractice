"""
https://programmers.co.kr/learn/courses/30/lessons/42841
모든 가능한 숫자에 대하여 주어진 질문과 답변을 대조함.
"""
from itertools import permutations

def test(x, y):
    x, y = list(x), list(y)
    s, b = 0, 0
    for i in range(3):
        if x[i] in y:
            if y.index(x[i]) == i: s += 1
            else: b += 1
    return [s, b]

def solution(baseball):
    targets = list(map(lambda x: str(x[0]), baseball))
    cond = list(map(lambda x: [x[1], x[2]], baseball))

    cases = list(permutations(range(1, 10), 3))
    cases = list(map(lambda x: list(map(str, x)), cases))

    answer = 0
    for x in cases:
        if [test(x, y) for y in targets] == cond: answer += 1

    return answer
