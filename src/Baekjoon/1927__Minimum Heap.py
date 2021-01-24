"""
https://www.acmicpc.net/problem/1927
Using heap
"""
#1. My Solution (152ms)
import sys
import heapq


input = sys.stdin.readline
hq = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if hq:
            print(hq[0])
            heapq.heappop(hq) 
        else:
            print(0)
    else:
        heapq.heappush(hq, n)
        
#2. Other Solution (124ms)
import heapq as h,sys;a=[];input()
for n in map(int,sys.stdin):h.heappush(a,n)if n else print(a and h.heappop(a)or 0)
