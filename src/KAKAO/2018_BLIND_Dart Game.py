"""
https://programmers.co.kr/learn/courses/30/lessons/17682/
"""
#1. My solution
from collections import deque


def solution(dartResult):
    q = deque(list(dartResult))

    flag_i = True
    score = []
    bonus = []
    option = []
    while q:
        if flag_i:
            first = q.popleft()
            if q[0] == '0':
                q.popleft()
                score.append(10)
            else:
                score.append(int(first))
            flag_i = False
        else:
            bonus.append(q.popleft())
            if len(q) > 0 and (q[0] == '*' or q[0] == '#'):
                option.append(q.popleft())
            else:
                option.append(0)
            flag_i = True

    dict_b = {'S':1, 'D':2, 'T':3}
    dict_o = {'*':2, '#':-1, 0:1}
    arr = []
    for i in range(3):
        a = score[i] ** dict_b[bonus[i]] * dict_o[option[i]]
        if option[i] == '*' and i > 0:
            arr[i-1] *= 2
        arr.append(a)

    return sum(arr)
    
#2. Using Regular Expression
# \d : [0-9]
# + : 1번 이상 반복
# ? : 있어도 되고 없어도 된다
# () : Grouping
import re


def solution(dartResult):
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)

    dict_b = {'S':1, 'D':2, 'T':3}
    dict_o = {'*':2, '#':-1, '':1}
    arr = []
    for i in range(3):
        a = int(dart[i][0]) ** dict_b[dart[i][1]] * dict_o[dart[i][2]]
        if dart[i][2] == '*' and i > 0:
            arr[i-1] *= 2
        arr.append(a)

    return sum(arr)
