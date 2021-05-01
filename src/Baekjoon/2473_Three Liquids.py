"""
https://www.acmicpc.net/problem/2473
Using binary search
Find minimum tuple of value for every element
"""
#1. My Solution (1960ms)
def solve():
    min_val = float('inf')
    min_ans = []
    for i in range(n-2):
        j, k = i+1, n-1
        while j < k:
            temp = arr[i] + arr[j] + arr[k]

            if temp == 0:
                return [arr[i], arr[j], arr[k]]
                
            if abs(temp) < min_val:
                min_val = abs(temp)
                min_ans = [arr[i], arr[j], arr[k]]
                
            if temp > 0:
                k -= 1
            else:
                j += 1
            
    return min_ans


n = int(input())
arr = [*map(int, input().split())]
arr.sort()

print(' '.join(map(str, solve())))
