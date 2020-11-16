"""
https://www.acmicpc.net/problem/9024
Using two pointer approach
"""
#1. My Solution
import sys


input = sys.stdin.readline
for _ in range(int(input().strip())):
    n, k = map(int, input().strip().split())
    arr = [*map(int, input().strip().split())]
    arr.sort()
    
    pivot = sys.maxsize
    ans = 0
    l = 0; r = n - 1
    while l < r:
        temp = abs(k - arr[r] - arr[l])
        if temp < pivot:
            pivot = temp
            ans = 1
        elif temp == pivot:
            ans += 1
        
        if arr[r] + arr[l] < k:
            l += 1
        else:
            r -= 1
        
    print(ans)
