"""
https://school.programmers.co.kr/learn/courses/30/lessons/138477
Using heap
"""
#1. My Solution
import heapq


def solution(k, score):
    answer = []
    h = []
    for s in score:
        if len(h) < k:
            heapq.heappush(h, s)
        elif s > h[0]:
            heapq.heappop(h)
            heapq.heappush(h, s)
        answer.append(h[0])
    return answer
