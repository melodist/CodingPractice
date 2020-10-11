"""
https://www.acmicpc.net/problem/2467
Using binary search
"""
#1. My Solution
import sys
import bisect


input = sys.stdin.readline
n = int(input().strip())
arr = [*map(int, input().strip().split())]

val = sys.maxsize
acid = 0
base = 0
for i, a in enumerate(arr):
    j = bisect.bisect_right(arr, -a)

    if j == n:
        b = arr[j-1] if a != arr[j-1] else arr[j-2]
        temp = abs(a+b)
    elif j == 0:
        b = arr[j] if a != arr[j] else arr[j+1]
        temp = abs(a+b)
    else:
        b = arr[j-1] if a != arr[j-1] else arr[j-2]
        c = arr[j] if a != arr[j] else arr[j+1]
        if abs(a+b) > abs(a+c):
            b = c
            temp = abs(a+c)
        else:
            temp = abs(a+b)
            
    if val > temp:
        acid, base = a, b
        val = temp
                
print(acid, base) if acid < base else print(base, acid)

#2. Other Solution
import sys
def solution(liq):
    l=0
    r=len(liq)-1
    ans = [abs(liq[l]+liq[r]),(liq[l],liq[r])]

    while l<r:
        mix = liq[l]+liq[r]
        if abs(mix) < ans[0]:
            ans[0] = abs(mix)
            ans[1] = (liq[l],liq[r])
        if mix > 0:
            r-=1
        elif mix < 0:
            l += 1
        else:
            return ans[1]
    return ans[1]

if __name__== "__main__":
    n = map(int,sys.stdin.readline().split())
    liq = list(map(int,sys.stdin.readline().split()))
    ans = solution(liq)
    print("{} {}".format(ans[0],ans[1]))
