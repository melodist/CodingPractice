"""
https://www.acmicpc.net/problem/11053
Longest Increasing Subsequence Problem
Using binary search

16
8 6 9 1 4 6 7 4 3 7 4 7 2 5 2 10
>> 5 : correct
>> 6 : when using bisect.bisect_right()
bisect_left() -> all(val < x for val in a[lo:i]) on left side
bisect_right() -> all(val <= x for val in a[lo:i]) on left side
lis should not have the same value for its elements
"""
import sys
import bisect


n = int(input())
a = [*map(int, sys.stdin.readline().strip().split())]

lis = [a[0]]

for i in range(1, n):
    # If a[i] is smallest, replace the value.
    if a[i] <= lis[0]:
        lis[0] = a[i]
    
    # If a[i] is biggest, put the value at last.
    elif a[i] > lis[-1]:
        lis.append(a[i])
    
    # Find lower bound for a[i] and replace the value for smaller one.
    else:
        lis[bisect.bisect_left(lis, a[i], 0, len(lis)-1)] = a[i]

print(len(lis))
