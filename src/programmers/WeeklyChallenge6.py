"""
https://programmers.co.kr/learn/courses/30/lessons/85002
Implementation Problem
"""
#1. My Solution
def solution(weights, head2head):
    info = []
    n = len(weights)
    for i in range(n):
        w = w2 = l = 0
        for j in range(n):   
            if i == j:
                continue
            if head2head[i][j] == 'W':
                w += 1
                if weights[i] < weights[j]:
                    w2 += 1
            elif head2head[i][j] == 'L':
                l += 1
        rate = w/(w+l) if w+l > 0 else 0
        info.append((rate, w2, weights[i], i))
    #1. 전체 승률 높음
    #2. 자기보다 무거운 선수 많이 이김
    #3. 자기 몸무게가 무거움
    #4. 작은 번호
    info.sort(key=lambda x:(-x[0], -x[1], -x[2], x[3]))
    return [x[3] + 1 for x in info]

#2. Other Solution
# basic sort is ascending order
def solution(weights, head2head):
    info = []
    n = len(weights)
    for i in range(n):
        w = w2 = l = 0
        for j in range(n):   
            if i == j:
                continue
            if head2head[i][j] == 'W':
                w += 1
                if weights[i] < weights[j]:
                    w2 += 1
            elif head2head[i][j] == 'L':
                l += 1
        rate = w/(w+l) if w+l > 0 else 0
        info.append((-rate, -w2, -weights[i], i))
    #1. 전체 승률 높음
    #2. 자기보다 무거운 선수 많이 이김
    #3. 자기 몸무게가 무거움
    #4. 작은 번호
    return [x[3] + 1 for x in sorted(info)]
