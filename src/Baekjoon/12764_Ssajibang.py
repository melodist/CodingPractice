"""
https://www.acmicpc.net/problem/12764
Using 3 primary queue
1st - sort users for start time
2nd - sort users for end time
3rd - manages free seat number
"""
#1. My Solution
# Mistake 1 : seat number should be minimal in blank seats
# Mistake 2 : hq_seat[0][0] > start -> only append record
# Counterexamples
# 5
# 20 100
# 10 40
# 30 50
# 60 110
# 80 90
import sys
import heapq


hq = []
for _ in range(int(input())):
    heapq.heappush(hq, [*map(int, sys.stdin.readline().strip().split())])

start, end = heapq.heappop(hq)
hq_seat = [(end, start, 0)]
hq_number = []
record = [1]
# print(start, end, 0, record)

while hq:
    start, end = heapq.heappop(hq)
    # Next user should sit free seat which has minimal number
    if hq_seat[0][0] > start:
        if not hq_number:
            record.append(1)
            seat_new = len(record) - 1
        else:
            seat_new = heapq.heappop(hq_number)
            record[seat_new] += 1
            
        heapq.heappush(hq_seat, (end, start, seat_new))
    else:
        # Pop all users whose end time is ealrier than start time
        while hq_seat and hq_seat[0][0] < start:
            _, _, seat = heapq.heappop(hq_seat)
            heapq.heappush(hq_number, seat)
            
        seat_new = heapq.heappop(hq_number)
        record[seat_new] += 1
        heapq.heappush(hq_seat, (end, start, seat_new))
    # print(start, end, seat_new, record)

print(len(record))
print(' '.join(map(str, record)))
