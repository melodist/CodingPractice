"""
https://www.hackerrank.com/challenges/mark-and-toys/problem
Using Quicksort and Greedy algorithm
"""
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

def maximumToys(prices, k):
    prices = quicksort(prices)
    total, i = 0, 0
    for p in prices:
        total += p
        if total > k:
            break
        i += 1
        
    return i
