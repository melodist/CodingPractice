"""
https://www.acmicpc.net/problem/2751
1. Merge Sort
"""
import sys

n = int(input())
a = [int(sys.stdin.readline().strip()) for _ in range(n)]

def merge(array, begin, end):
    if begin < end:
        mid = (begin + end) // 2
        # Divide
        if begin != end - 1:
            merge(array, begin, mid)
            merge(array, mid+1, end)
        
        # Conquer
        i, j, k = begin, mid+1, 0
        temp = [0] * (end - begin + 1)
        while i < mid+1 and j < end+1:
            if array[i] < array[j]:
                temp[k] = array[i]
                i += 1
                k += 1
            else:
                temp[k] = array[j]
                j += 1
                k += 1
        
        if i == mid+1:
            temp[k:] = array[j:end+1]
        else:
            temp[k:] = array[i:mid+1]

        array[begin:end+1] = temp[:]

merge(a, 0, n-1)
[print(num) for num in a]
