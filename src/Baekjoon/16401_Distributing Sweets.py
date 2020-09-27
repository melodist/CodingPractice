"""
https://www.acmicpc.net/problem/16401
Using binary search
"""
#1. My Solution
def check(pivot, arr):
  return sum([a // pivot for a in arr])
    
MAX = 10**9
m, n = map(int, input().split())
arr = [*map(int, input().split())]
left = 1; right = MAX
while left <= right:
    mid = (left + right) // 2
    if check(mid, arr) >= m:
        left = mid + 1
    else:
        right = mid - 1
        
print(left-1)
