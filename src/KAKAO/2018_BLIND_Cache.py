"""
https://programmers.co.kr/learn/courses/30/lessons/17680
"""
from collections import deque


def solution(cacheSize, cities):
    q = deque([], maxlen=cacheSize)
    answer = 0
    for city in cities:
        city = city.lower()
        if city in q:
            answer += 1
            q.remove(city)
            q.append(city)
        else:
            answer += 5
            if cacheSize > 0:
                q.append(city)

    return answer
