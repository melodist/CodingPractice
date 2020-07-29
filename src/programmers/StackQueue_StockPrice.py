"""
https://programmers.co.kr/learn/courses/30/lessons/42584/
"""
#1. My Solution
def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    for t, p in enumerate(prices):
        while stack and stack[-1][1] > p:
            x, y = stack.pop()
            answer[x] = t - x
        stack.append((t, p))

    while stack:
        x, y = stack.pop()
        answer[x] = n - 1 - x

    return answer

#2. Other Solution
from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer
