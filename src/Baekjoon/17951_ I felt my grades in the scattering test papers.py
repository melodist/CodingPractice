"""
https://www.acmicpc.net/problem/17951
Using Parametric Search (application of binary search)
"""
#1. My Solution
import sys


n, k = map(int, input().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

start = 0
end = sum(arr)
ans = -1
ms = float('inf')

while start <= end:
    mid = (start + end) // 2
    diff = float('inf')
    cnt = 1
    flag = False
    
    ms = 0    
    for i in range(n):
        ms += arr[i]
        if ms >= mid:
            diff = min(diff, ms)
            ms = 0
            cnt += 1
            if cnt > k:
                ans = max(ans, diff)
                flag = True
                break
            
    if flag:
        start = mid + 1
        ans = max(ans, diff)
    else:
        end = mid - 1
        
print(ans)

#2. Other Solution (https://www.acmicpc.net/source/16146238)
# s : sum / c : count / u : lower bound / v : upper bound / p(x) : parametric search for x
def p(x):
  s=0; c=0
  for i in a:
    s+=i
    if s>=x:
      c+=1; s=0
  return c>=k
  
  
n,k=map(int,input().split())
a=[*map(int,input().split())]

u=0; v=sum(a)//k+1

while v-u>1:
  m=(v+u)//2
  if p(m): u=m
  else: v=m
print(u)
