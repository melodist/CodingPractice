"""
https://www.hackerrank.com/challenges/angry-children/problem
Using greedy algorithm
"""
#1. My Solution
def maxMin(k, arr):
    arr.sort()
    print(arr)
    a_min = arr[0]
    a_max = arr[k-1]
    ans = a_max - a_min
    for a in range(1, len(arr)-k+1):
        ans = min(ans, arr[a+k-1] - arr[a])

    return ans
