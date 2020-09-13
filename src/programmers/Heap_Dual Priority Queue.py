"""
https://programmers.co.kr/learn/courses/30/lessons/42628
Using priority queue and hashmap
"""
#1. My Solution
import heapq
from collections import defaultdict

def solution(operations):
    maxi = []
    mini = []
    dic = defaultdict(int)
    for o in operations:
        if o[0] == 'I':
            _, n = o.split()
            n = int(n)
            heapq.heappush(maxi, -n)
            heapq.heappush(mini, n)
            dic[n] += 1
        else:
            if dic.keys():
                _, k = o.split()
                if k == '1':
                    i = -heapq.heappop(maxi)
                    while i not in dic:
                        i = -heapq.heappop(maxi)
                    if dic[i] == 1:
                        del dic[i]
                    else: dic[i] -= 1
                else:
                    i = heapq.heappop(mini)
                    while i not in dic:
                        i = heapq.heappop(mini)
                    if dic[i] == 1:
                        del dic[i]
                    else: dic[i] -= 1

    if len(dic.keys()) > 0:
        a = -heapq.heappop(maxi)
        while maxi and a not in dic:
            a = -heapq.heappop(maxi)
            
        b = heapq.heappop(mini)
        while mini and b not in dic:
            b = heapq.heappop(mini)      
        return a, b
    else:
        return 0, 0
        
#2. Other Solution
import heapq

def solution(operations):
    heap = []

    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap:
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]
