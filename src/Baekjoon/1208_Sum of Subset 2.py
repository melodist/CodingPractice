"""
https://www.acmicpc.net/problem/1208
Using bit mask and two-pointer approach
"""
#1. Solution using Pypy3 (888ms)
n, s = map(int, input().split())
a = [*map(int, input().split())]

half = n // 2
first_half = [0] * (1 << (n - half))
second_half = [0] * (1 << half)

for i in range(1 << (n - half)):
    for j in range(n - half):
        if (1 << j) & i:
            first_half[i] += a[j]
            
for i in range(1 << half):
    for j in range(half):
        if (1 << j) & i:
            second_half[i] += a[j + (n - half)]

first_half.sort()
second_half.sort(reverse=True)

ans = 0
idx1, idx2 = 0, 0
while idx1 < 1 << (n - half) and idx2 < 1 << half:
    if first_half[idx1] + second_half[idx2] == s:
        cnt1, cnt2 = 1, 1
        idx1 += 1
        idx2 += 1
        while idx1 < 1 << (n-half) and first_half[idx1] == first_half[idx1-1]:
            idx1 += 1
            cnt1 += 1
        while idx2 < 1 << half and second_half[idx2] == second_half[idx2-1]:
            idx2 += 1
            cnt2 += 1
        ans += cnt1 * cnt2
        
    elif first_half[idx1] + second_half[idx2] < s:
        idx1 += 1
    else:
        idx2 += 1

print(ans-1 if s == 0 else ans)

#2. Other Solution using Python3 (832ms)
from collections import Counter
import sys
f = lambda : map(int, sys.stdin.readline().split())

n, s = f()
box, m = [*f()], n//2
a_list, b_list = box[0:m], box[m::]
a, b = [0], [0]

def extend(o, l):
    for i in l:
        tmp = [j+i for j in o]
        o += tmp
extend(a, a_list)
extend(b, b_list)
b_counter = Counter(b)

cnt = 0 if s != 0 else -1
for i in a:
    if s-i in b_counter:
        cnt += b_counter[s-i]
print(cnt)
