"""
https://www.acmicpc.net/problem/1806
Using two pointers approach
"""
#1. My Solution (160ms)
import sys


input = sys.stdin.readline
n, s = map(int, input().split())
a = [*map(int, input().split())]

l = r = 0
ans = n+1
curr = a[0]

while l <= r:
    if curr >= s:
        ans = min(ans, r - l + 1)
        curr -= a[l]
        l += 1
    else:
        if r < n-1:
            r += 1
            curr += a[r]
        elif r == n-1:
            break

print(ans if ans < n+1 else 0)

#2. Other Solution (120ms)
import sys
input = sys.stdin.readline

def main():
  n, s = map(int, input().split())
  a = list(map(int, input().split()))
  hi, lo = 0, 0
  temp = 0
  length = []

  while True:
    if temp >= s:
      length.append(hi-lo)
      temp -= a[lo]
      lo += 1
    elif hi == n:
      break
    elif temp < s:
      temp += a[hi]
      hi += 1

  if length:
    print(min(length))
  else:
    print(0)
  
main()
