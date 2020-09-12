"""
https://www.acmicpc.net/problem/7795
Using two pointer approach
"""
#1. Solution using two pointer
import sys


for _ in range(int(input())):
    n, m = map(int, input().split())
    A = sorted([*map(int, sys.stdin.readline().strip().split())], reverse=True)
    B = sorted([*map(int, sys.stdin.readline().strip().split())], reverse=True)
    
    answer, a, b = 0, 0, 0
    while a < n and b < m:
        if A[a] > B[b]:
            a += 1
        else:
            answer += a
            b += 1
            
    if b < m:
        answer += (m-b) * n
        
    print(answer)
    
#2. Solution using binary search
import sys
import bisect

for _ in range(int(input())):
    n, m = map(int, input().split())
    A = sorted([*map(int, sys.stdin.readline().strip().split())])
    B = [*map(int, sys.stdin.readline().strip().split())]
    
    answer = 0
    for i in range(m):
        answer += n - bisect.bisect_right(A, B[i])
        
    print(answer)
