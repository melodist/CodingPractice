"""
https://www.acmicpc.net/problem/2166
Using Outer Product
"""
#1. My Solution (84ms)
import sys

def ccw(a, b, c):
    v1 = (b[0] - a[0], b[1] - a[1])
    v2 = (c[0] - a[0], c[1] - a[1])
    return 0.5 * (v1[0] * v2[1] - v1[1] * v2[0])


input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
    
ans = 0
for i in range(1, n-1):
    ans += ccw(arr[0], arr[i], arr[i+1])
    
#2. Other Solution (68ms)
import sys
I=sys.stdin.readline
n=int(input())
a=[]
b=[]
for i in range(n):
	x,y=map(int,I().split())
	a.append(x)
	b.append(y)
a.append(a[0])
b.append(b[0])
s=0
for i in range(n):
	s+=a[i]*b[i+1]-a[i+1]*b[i]
s=abs(s)/2
print("%0.1f"%round(s,1))
