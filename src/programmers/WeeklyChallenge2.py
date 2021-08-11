"""
https://programmers.co.kr/learn/courses/30/lessons/83201
Implementation Problem
"""
from collections import Counter


def solution(scores):
    answer = ''
    n = len(scores)

    scores = list(zip(*scores))

    for i in range(n): 
        if max(scores[i]) == scores[i][i] or min(scores[i]) == scores[i][i] :
            c = Counter(scores[i])
            if c[scores[i][i]] == 1:
                avg = (sum(scores[i]) - scores[i][i]) / (n-1)
            else:
                avg = sum(scores[i]) / n
        else:
            avg = sum(scores[i]) / n

        if avg >= 90:
            s = 'A'
        elif avg >= 80:
            s = 'B'
        elif avg >= 70:
            s = 'C'
        elif avg >= 50:
            s = 'D'
        else:
            s = 'F'

        answer += s
    return answer
