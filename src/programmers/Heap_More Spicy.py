"""
https://programmers.co.kr/learn/courses/30/lessons/42626
Using heapq
Count the condition with length = 1 and meets the condition.
"""
import heapq

    
def solution(scoville, K):
    heapq.heapify(scoville)
    
    answer = 0
    while len(scoville) > 1:
        if scoville[0] >= K:
            return answer
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        heapq.heappush(scoville, first + second * 2)
        
        answer += 1
    
    print(scoville)
    return -1 if scoville[0] < K else answer
