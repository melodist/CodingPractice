"""
"""
#1. My Solution
import re
from itertools import permutations


def calc(a, b, op):
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    else:
        return a - b

def solution(expression):
    ops = re.findall('[^0-9]', expression)
    digits = re.findall('[0-9]+', expression)
    digits = [int(d) for d in digits]
    order = [
        ['*', '+', '-'],
        ['*', '-', '+'],
        ['+', '*', '-'],
        ['+', '-', '*'],
        ['-', '*', '+'],
        ['-', '+', '*']
    ]


    answer = 0
    for o in order:
        _digits = digits
        _ops = ops

        for i in range(3):
            if not _ops:
                break

            stack_d = [_digits[0]]
            stack_o = []

            for j in range(len(_ops)):
                stack_d.append(_digits[j+1])
                stack_o.append(_ops[j])

                if stack_o[-1] == o[i]:
                    a = stack_d.pop()
                    b = stack_d.pop()
                    op = stack_o.pop()

                    stack_d.append(calc(b, a, op))

            _digits = stack_d
            _ops = stack_o

        answer = max(answer, abs(_digits[0]))

    return answer
    
#2. Other Solution
import re
from itertools import permutations

def solution(expression):
    #1
    op = [x for x in ['*','+','-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    ex = re.split(r'(\D)',expression) # \D : non-digit

    #2
    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1])) # eval() : 문자열을 코드로 인식하게 하는 함수
                _ex = _ex[:tmp]+_ex[tmp+2:]
        a.append(_ex[-1])

    #3
    return max(abs(int(x)) for x in a)
