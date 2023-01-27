"""
https://school.programmers.co.kr/learn/courses/30/lessons/154539
Using heap
"""
#1. My Solution
import heapq


def solution(numbers):
    hq = []

    for i, n in enumerate(numbers):
        # Replace value at index which has smaller value than n
        while hq and hq[0][0] < n:
            value, index = heapq.heappop(hq)
            numbers[index] = n
            
        heapq.heappush(hq, (n, i))
        
    # Replace left index with -1
    while hq:
        _, i = heapq.heappop(hq)
        numbers[i] = -1
    
    return numbers
