"""
https://www.acmicpc.net/problem/2631
Find Longest Increasing Subsequence Size
"""
def lower_bound(A, left, right, key):
    while right - left > 1:
        mid = left + (right - left) // 2
        if A[mid] >= key: right = mid
        else: left = mid
        
    return right

n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
    
lis = [0 for i in range(n+1)]

lis[0] = a[0]
pos = 1

for i in range(1, n):
    # If a[i] is smallest, replace the value.
    if a[i] < lis[0]:
        lis[0] = a[i]
    
    # If a[i] is biggest, put the value at last.
    elif a[i] > lis[pos-1]:
        lis[pos] = a[i]
        pos += 1
    
    # Find lower bound for a[i] and replace the value for smaller one.
    else:
        lis[lower_bound(lis, -1, pos-1, a[i])] = a[i]
        
print(n - pos)
