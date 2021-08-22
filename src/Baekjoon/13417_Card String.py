"""
https://www.acmicpc.net/problem/13417
String Problem
"""
#1. My Solution (112ms)
import sys


input = sys.stdin.readline
for _ in range(int(input())):
    t = int(input())
    arr = input().split()
    
    ans = arr[0]
    for c in arr[1:]:
        if ans[0] >= c:
            ans = c + ans
        else:
            ans += c
            
    print(ans)
