"""
https://www.acmicpc.net/problem/14003
Longest Increasing Sequence (LIS) Problem
"""
#1. My Solution (1692ms)
import bisect


n = int(input())
arr = [*map(int, input().split())]

temp = []
val = []
ind = []
for i, a in enumerate(arr):
    if not temp or a > temp[-1]:
        temp.append(a)
        val.append(a)
        ind.append(len(temp)-1)
    else:
        j = bisect.bisect_left(temp, a)
        temp[j] = a
        val.append(a)
        ind.append(j)

ans = []
m = len(temp) - 1
for v, i in zip(val[::-1], ind[::-1]):
    if i == m:
        ans.append(v)
        m -= 1
        
print(len(ans))
print(' '.join(map(str, ans[::-1])))
