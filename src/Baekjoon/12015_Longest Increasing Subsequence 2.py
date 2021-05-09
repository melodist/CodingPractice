"""
https://www.acmicpc.net/problem/12015
Longest Increasing Subsequence Problem
Using binary search
"""
#1. My Solution(1048ms)
import sys
import bisect


input = sys.stdin.readline
n = int(input())
A = [*map(int, input().split())]
LIS = [A[0]]

for a in A[1:]:
    if a > LIS[-1]:
        LIS.append(a)
    else:
        lower_bound = bisect.bisect_left(LIS, a)
        LIS[lower_bound] = a

print(len(LIS))
