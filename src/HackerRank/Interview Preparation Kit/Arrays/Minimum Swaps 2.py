"""
https://www.hackerrank.com/challenges/minimum-swaps-2/problem
"""
def minimumSwaps(arr):
    arr_sorted = sorted(arr)
    ans = 0
    index = {val:key for key, val in enumerate(arr)}

    for i in range(n):
        a, b = arr[i], arr_sorted[i]
        if a != b:
            arr[index[b]], arr[i] = arr[i], arr[index[b]]
            index[a], index[b] = index[b], i
            ans += 1
            
    return ans
