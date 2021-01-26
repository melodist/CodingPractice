"""
https://www.acmicpc.net/problem/11286
Using minimum heap and pair
"""
#1. My Solution (168ms)
import sys
import heapq


input = sys.stdin.readline
hq = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if hq:
            a, b = heapq.heappop(hq)
            print(b)
        else:
            print(0)
    else:
        heapq.heappush(hq, (abs(n), n))
