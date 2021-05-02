"""
https://www.acmicpc.net/problem/1202
Using Priority Queue
"""
#1. My Solution (1380ms)
import sys
import heapq


input = sys.stdin.readline
n, k = map(int, input().split())
gems = []
bags = []

for _ in range(n):
    m, v = map(int, input().split())
    gems.append((m, v))

for _ in range(k):
    bags.append(int(input().strip()))
    
gems.sort()
bags.sort()

pq = []
ans = 0
j = 0
for i in range(k):
    while j < n and gems[j][0] <= bags[i]:
        heapq.heappush(pq, -gems[j][1])  # If gems[j] is lighter than bags[i], it can be put in any bag which is heavier than bags[i]
        j += 1
    
    if pq:
        ans -= pq[0]
        heapq.heappop(pq)

print(ans)
