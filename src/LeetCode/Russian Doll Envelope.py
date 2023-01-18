"""
https://leetcode.com/problems/russian-doll-envelopes
Using Binary Search and Sort
"""
#1. My Solution (1622ms)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        top = []

        for _, h in envelopes:
            left = 0
            right = len(top)

            while left < right:
                mid = int((left + right) / 2)
                if top[mid] > h:
                    right = mid
                elif top[mid] < h:
                    left = mid + 1
                else:
                    right = mid

            if left == len(top):
                top.append(h)
            else:
                top[left] = h


        return len(top)
