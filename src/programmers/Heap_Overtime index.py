"""
https://programmers.co.kr/learn/courses/30/lessons/12927?language=python3#
Using maximum heap
"""
#1. My Solution
import heapq


def solution(n, works):
    hq = []
    for w in works:
        heapq.heappush(hq, -w)

    answer = 0
    while n > 0:
        a = heapq.heappop(hq)
        if a == 0: 
            break
        heapq.heappush(hq, a+1)
        n -= 1
        
    return sum([i*i for i in hq])
