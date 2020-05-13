"""
https://www.hackerrank.com/challenges/mark-and-toys/problem
Using Quicksort and Greedy algorithm
"""
#1. Simple Quicksort
def quicksort(arr):
    n = len(arr)
    if n == 0 or n == 1: return arr
    pivot = arr[n//2]
    arr = arr[:n//2] + arr[n//2+1:]
    left, right = [], []
    for x in arr:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
            
    return quicksort(left) + [pivot] + quicksort(right)

#2. In-place Quicksort
def quicksort(low, high):
    if low >= high:
        return
    
    mid = partition(low, high)
    quicksort(low, mid - 1)
    quicksort(mid, high)

def partition(low, high):
    pivot = prices[(low + high) // 2]
    while low <= high:
        while prices[low] < pivot:
            low += 1
        while prices[high] > pivot:
            high -= 1
        if low <= high:
            prices[low], prices[high] = prices[high], prices[low]
            low, high = low + 1, high - 1
            
    return low


def maximumToys(prices, k):
    prices = quicksort(prices)
    # quicksort(0, len(prices) - 1)
    total, i = 0, 0
    for p in prices:
        total += p
        if total > k:
            break
        i += 1
        
    return i
