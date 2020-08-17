"""
https://programmers.co.kr/learn/courses/30/lessons/42891
Using Min Heap
1. Make Priority Queue using Min Heap
2. Delete Minimum food time * length of foods as k > 0
3. Find index for left foods
"""
import heapq


def solution(food_times, k):
    if k >= sum(food_times): return -1

    heap = []
    for i, x in enumerate(food_times):
        heapq.heappush(heap, (x, i+1))

    prev = 0
    # Delete Minimum food time * length of foods
    while k - (heap[0][0] - prev) * len(heap) > 0:
        k -= (heap[0][0] - prev) * len(heap)
        prev = heapq.heappop(heap)[0]
    
    # Sort heap by index
    heap.sort(key=lambda x: x[1])

    return heap[k % len(heap)][1]
