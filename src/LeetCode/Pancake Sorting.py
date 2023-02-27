"""
https://leetcode.com/problems/pancake-sorting
Using recursion
"""
#1. My Solution (44ms)
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def sort(arr, n):
            if n == 1: return arr

            # Find max index
            i = arr.index(max(arr[:n]))

            arr = reverse(arr, 0, i)
            res.append(i+1)
            arr = reverse(arr, 0, n-1)
            res.append(n)

            return sort(arr, n-1)

        def reverse(arr, start, end):
            return arr[:start] + arr[start:end+1][::-1] + arr[end+1:]

        res = []
        sort(arr, len(arr))

        return res
      
#2. Other Solution (34ms)
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for x in range(len(arr), 1, -1):
            i = arr.index(x)
            res.extend([i + 1, x])
            arr = arr[:i:-1] + arr[:i]
        return res
