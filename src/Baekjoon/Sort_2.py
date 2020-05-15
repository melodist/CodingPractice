"""
https://www.acmicpc.net/problem/2751
1. Merge Sort
2. Heap Sort
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


# 2. Heap Sort
v = [int(sys.stdin.readline().rstrip()) for _ in range(int(input())]
 
def heapify(li, idx, n):
    l = idx * 2;
    r = idx * 2 + 1
    s_idx = idx
    if (l <= n and li[s_idx] > li[l]):
        s_idx = l
    if (r <= n and li[s_idx] > li[r]):
        s_idx = r
    if s_idx != idx:
        li[idx], li[s_idx] = li[s_idx], li[idx]
        return heapify(li, s_idx, n)
 
def heap_sort(v) :
    n = len(v)
    v = [0]+v
 
    # create min heap
    for i in range(n, 0, -1) :
        heapify(v, i, n)
 
    # min element extract & heap
    for i in range(n, 0, -1) :
        print(v[1])
        v[i], v[1] = v[1], v[i]
        heapify(v, 1, i-1)
 
heap_sort(v)
