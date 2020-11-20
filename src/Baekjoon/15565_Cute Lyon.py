"""
https://www.acmicpc.net/problem/15565
Using two pointer approach
"""
#1. My Solution
import sys


input = sys.stdin.readline
def solve():
    n, k = map(int, input().strip().split())
    a = [*map(int, input().strip().split())]

    if n == 1:
        return 1 if a[0] == 1 else -1

    ans = sys.maxsize
    l = r = 0
    count = 1 if a[0] == 1 else 0
        
    while True:
        if count >= k:
            ans = min(ans, r - l + 1)
            if a[l] == 1:
                count -= 1
            l += 1
        else:
            if r < n-1:
                r += 1
                if a[r] == 1:
                    count += 1
            else:
                break
            
    return ans if ans < sys.maxsize else -1
        
print(solve())

#2. Other Solution
N,K = map(int, input().split())
arr = input().split()

if arr.count('1') < K :
    print(-1)
else:
    lion = [i for i, x in enumerate( arr ) if x == '1']
    print(min(lion[K-1+j] - lion[j] + 1 for j in range(len(lion)-K+1)))
