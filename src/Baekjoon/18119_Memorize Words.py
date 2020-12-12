"""
https://www.acmicpc.net/problem/18119
Using bit mask
"""
#1. My Soltuion (3836ms - Pypy3)
import sys


input = sys.stdin.readline
n, m = map(int, input().split())
codes = []
keys = 2**26 - 1
a = ord('a')

for i in range(n):
    s = input().strip()
    code = 0
    for c in s:
        key = 1<<(ord(c) - a)
        if key & code != key:
            code |= key
    codes.append(code)

for _ in range(m):
    o, x = input().split()
    if o == '1':
        keys ^= 1<<(ord(x) - a)
    else:
        keys |= 1<<(ord(x) - a)
        
    ans = 0
    for i in range(n):
        if codes[i] & keys == codes[i]:
            ans += 1
            
    print(ans)
    
#2. Other Solution (1128ms - Pypy3)
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[[] for _ in range(26)]
for i in range(n):
  w=set(input().rstrip())
  for x in w:
    a[ord(x)-97].append(i)
c=[0]*n
ans=n
for _ in range(m):
  o,x=input().split()
  if o=='1':
    for i in a[ord(x)-97]:
      if c[i]==0:
        ans-=1
      c[i]+=1
  else:
    for i in a[ord(x)-97]:
      c[i]-=1
      if c[i]==0:
        ans+=1
  print(ans)
