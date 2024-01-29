"""
https://www.acmicpc.net/problem/23254
Using greedy algorithm
Maximize score increase
"""
#1. My Solution (1168ms)
import sys, heapq

n, m = map(int, sys.stdin.readline().strip().split())
a = [int(i) for i in sys.stdin.readline().strip().split()]
b = [int(i) for i in sys.stdin.readline().strip().split()]

# Sort subjects by score increase
pq = []
for i in range(m):
    if a[i] + b[i] < 100:
        heapq.heappush(pq, (-b[i], i))
    else:
        heapq.heappush(pq, (a[i] - 100, i))
        
t = 0
MAX_TIME = n * 24
while t < MAX_TIME:
    if not pq:
        break
    
    (minus_increase, i) = heapq.heappop(pq)
    
    if (a[i] - 100 == minus_increase):
        t += 1
        a[i] = 100
        continue
    
    t_increase = (100 - a[i]) // (-minus_increase) if (100 - a[i]) // (-minus_increase) + t <= MAX_TIME else MAX_TIME - t

    a[i] += t_increase * (-minus_increase)
    t += t_increase
    
    if a[i] - 100 >= minus_increase:
        heapq.heappush(pq, (a[i] - 100, i))
    else:
        heapq.heappush(pq, (minus_increase, i))
        
print(sum(a))
