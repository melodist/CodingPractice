"""
https://www.hackerrank.com/challenges/queries-with-fixed-length/problem
Minimax Problem
"""
#1. My Solution
from collections import deque


def solve(arr, queries):
    result = []
    n = len(arr)

    for d in queries:
        if d == n:
            result.append(max(arr))
        elif d == 1:
            result.append(min(arr))
        else:
            q = deque(arr[:d])
            val_max = max(q)
            val_min = val_max
            for i in range(d, n):
                shifted = q.popleft()
                if shifted == val_max:
                    val_max = max(q)
                
                appended = q.append(arr[i])
                val_max = max(arr[i], val_max)
                val_min = min(val_max, val_min)

            result.append(val_min)
    return result
    
#2. Optimal Solution
import collections 


def solve(arr, queries):
    arrLength = len(arr)
    mins = []

    for d in queries:
        maxes = []
        queue = collections.deque()

        # Process first d (size of window) elements
        for i in range(d):
            # If bigger element found for current window, pop rest of elements
            while len(queue) != 0 and arr[i] >= arr[queue[-1]]: queue.pop()
            queue.append(i)     # Add element to queue

        # Process rest of elements: arr[d] to arr[n-1]
        for i in range(d, arrLength):
            maxes.append(arr[queue[0]]) # Largest element of previous window

            # Remove elements outside of this window
            while len(queue) != 0 and queue[0] <= i - d:
                queue.popleft()

            # Remove elements smaller than current 
            while len(queue) != 0 and arr[i] >= arr[queue[-1]]: queue.pop()

            queue.append(i)     # Add element to queue
        
        maxes.append(arr[queue[0]]) # Largest element of last window
        mins.append(min(maxes))     # Add minimum for current window size
    
    return mins
