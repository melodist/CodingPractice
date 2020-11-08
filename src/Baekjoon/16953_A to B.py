"""
https://www.acmicpc.net/problem/16953
Using BFS
"""
#1. My Solution
from collections import deque


def bfs(a, b):
    q = deque([(a, 1)])
    while q:
        u, v = q.popleft()
        if u == b:
            return v
        
        if u * 2 <= b:
            q.append((u*2, v+1))
            
        if u * 10 + 1 <= b:
            q.append((u*10+1, v+1))
    
    return -1
    
a, b = map(int, input().split())
print(bfs(a, b))

#2. Other Solution using bottom-up
n,m = map(int,input().split())
count=0
while n!=m:
    if n>m:
        count=-2
        break
    elif str(m)[-1]=='1':
        m=m//10
        count+=1
    elif m%2==0:
        m=m//2
        count+=1
    else:
        count=-2
        break
print(count+1)
