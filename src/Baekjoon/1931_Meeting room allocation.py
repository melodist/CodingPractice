"""
https://www.acmicpc.net/problem/1931
Using greedy algorithm
Sort array by end time
"""
#1. My Solution (284ms)
import sys


input = sys.stdin.readline
n = int(input())
meets = []
for _ in range(n):
    meets.append(tuple(map(int, input().split())))
    
meets.sort(key=lambda x:(x[1], x[0]))
ans = 0
ends = -1

for u, v in meets:
    if u >= ends:
        ans += 1
        ends = v
        
print(ans)

#2. Other Solution (244ms)
import sys
In =sys.stdin.readline

N = int(In())
meet =[(*map(int, In().split()),) for i in range(N)]

meet.sort()

cnt =0
start=float('inf')

for time in reversed(meet):
   if time[1] <= start:
       start = time[0]
       cnt +=1

print(cnt)
