"""
https://www.acmicpc.net/problem/5639
Using recursion
"""
#1. My Solution (96ms)
import sys
import bisect

sys.setrecursionlimit(10**9)
a = []
for line in sys.stdin:
    a.append(int(line))

# T-L-R -> L-R-T
def solve(l, r, a):
    if l == r:
        print(a[l])
        return
    elif l > r:
        return
    
    mid = bisect.bisect_right(a, a[l], l+1, r+1)
        
    solve(l+1, mid-1, a)
    solve(mid, r, a)
    print(a[l])
    
solve(0, len(a)-1, a)
