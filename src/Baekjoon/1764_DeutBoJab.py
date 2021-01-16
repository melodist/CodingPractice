"""
https://www.acmicpc.net/problem/1764
Implementation Problem
"""
#1. My Solution (136ms)
import sys


input = sys.stdin.readline
n, m = map(int, input().split())
deut = set()
bo = set()
for _ in range(n):
    deut.add(input().strip())
for _ in range(m):
    bo.add(input().strip())
    
ans = []
if n < m:
    deut, bo = bo, deut
    
for i in bo:
    if i in deut:
        ans.append(i)
        
ans.sort()
print(len(ans))
[print(i) for i in ans]

#2. Other Solution (84ms)
import sys
n, m = map(int, input().split())
nameList = sys.stdin.read().splitlines()
hearset = set(nameList[:n])
seeset = set(nameList[n:])
ret = list(hearset & seeset)
ret.sort()
print(len(ret))
for i in ret:
    print(i)
