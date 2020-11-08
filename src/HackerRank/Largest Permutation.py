"""
https://www.hackerrank.com/challenges/largest-permutation/
Using greedy algorithm
"""
#1. My Solution
def largestPermutation(k, arr):
    n = len(arr)
    ind = [0] * (n+1)
    for i, x in enumerate(arr):
        ind[x] = i
        
    temp = 0
            
    for i in range(n):
        if arr[i] != n - i and temp < k:
            swap = ind[n - i]
            arr[i], arr[swap] = arr[swap], arr[i]
            ind[n - i], ind[arr[swap]] = i, swap
            temp += 1

    return arr
