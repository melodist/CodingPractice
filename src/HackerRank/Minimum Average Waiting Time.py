"""
https://www.hackerrank.com/challenges/minimum-average-waiting-time/problem
Using greedy algorithm and minimum heap
"""
from heapq import heappush, heappop


def minimumAverage(customers):
    n = len(customers)
    customers.sort(reverse=True)
    pq = []
    time_waiting = 0
    current_time = 0

    while customers or pq:
        while customers and customers[-1][0] <= current_time:
            heappush(pq, customers.pop()[::-1])
        if pq:
            current_task = heappop(pq)
            current_time += current_task[0]
            time_waiting += current_time - current_task[1]
        else:
            heappush(pq, customers.pop()[::-1])
            current_time = pq[0][1]

    return time_waiting // n
