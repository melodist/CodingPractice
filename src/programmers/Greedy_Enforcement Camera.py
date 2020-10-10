"""
https://programmers.co.kr/learn/courses/30/lessons/42884
Using priority queue
"""
#1. My Soltuion
import heapq


def solution(routes):
    routes.sort()
    intervals = []
    for start, end in routes:
        if intervals:
            start_prev, end_prev = intervals[0]
            start_prev = -start_prev
            if end_prev >= start:
                heapq.heappop(intervals)
                start = max(start_prev, start)
                end = min(end_prev, end)
        heapq.heappush(intervals, (-start, end))

    return len(intervals)
    
#2. Other Solution
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer
