"""
https://www.acmicpc.net/problem/7662
Using priority queue
"""
#1. My Solution
import sys
import heapq


input = sys.stdin.readline
for _ in range(int(input().strip())):
    hq_min = []
    hq_max = []
    popped = set()
    ind = 0
    for _ in range(int(input().strip())):
        c, i = input().strip().split()

        if c == 'I':
            i = int(i)
            heapq.heappush(hq_min, (i, ind))
            heapq.heappush(hq_max, (-i, ind))
            ind += 1
        else:
            if i == '1':
                while hq_max and hq_max[0][1] in popped:
                    _, j = heapq.heappop(hq_max)
                if hq_max:
                    _, j = heapq.heappop(hq_max)
                    popped.add(j)
            else:
                while hq_min and hq_min[0][1] in popped:
                    _, j = heapq.heappop(hq_min)
                if hq_min:
                    _, j = heapq.heappop(hq_min)
                    popped.add(j)

    hq_ret = []
    while hq_min:
        val, ind = heapq.heappop(hq_min)
        if ind not in popped:
            ret_max = val
            heapq.heappush(hq_ret, val)
            
    if hq_ret:
        print(ret_max, hq_ret[0])
    else:
        print('EMPTY')
        
#2. Solution using binary search
import bisect
import sys
from collections import deque
input = sys.stdin.readline

pq = deque()
pqDict = dict()
for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == 'I':
        val = int(cmd[1])
        if val not in pqDict:
            bisect.insort_left(pq, val)
            pqDict[val] = 1
        else:
            pqDict[val] += 1
    else:
        if not pq:
            continue
        if cmd[1] == '1':
            if (v := pqDict[pq[-1]]) > 1:  # the walrus operator: v = pqdict[pq[-1]], if v > 1:
                pqDict[pq[-1]] = v-1
            else:
                pqDict.pop(pq[-1])
                pq.pop()
        else:
            if (v := pqDict[pq[0]]) > 1:
                pqDict[pq[0]] = v-1
            else:
                pqDict.pop(pq[0])
                pq.popleft()
if not pq:
    print("EMPTY")
else:
    print(pq[-1], pq[0])
