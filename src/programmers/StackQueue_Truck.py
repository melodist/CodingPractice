"""
https://programmers.co.kr/learn/courses/30/lessons/42583
"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    t = 0
    q = deque(truck_weights)
    on = deque([])
    timer = deque([])
    while q:
        if sum(on) + q[0] <= weight:
            on.append(q.popleft())
            timer.append(t + bridge_length)
        
        t += 1
        
        if timer[0] == t:
            on.popleft()
            timer.popleft()
            
    return timer[-1]+1
