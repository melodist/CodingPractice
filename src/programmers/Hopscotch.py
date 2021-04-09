"""
https://programmers.co.kr/learn/courses/30/lessons/12913
Using Dynamic Programming
"""
#1. My Solution
def solution(land):
    n = len(land)
    prev = land[0]
    next = [0] * 4
    for i in range(1, n):
        for j in range(4):
            temp = 0
            for k in range(4):
                if j == k:
                    continue
                temp = max(temp, prev[k])
            next[j] += temp + land[i][j]
        prev = next
        next = [0] * 4

    return max(prev)

#2. Other Solution
def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])
