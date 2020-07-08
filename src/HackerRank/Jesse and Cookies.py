"""
https://www.hackerrank.com/challenges/jesse-and-cookies/problem
"""
#1. My Solution
import heapq


def cookies(k, A):
    n = len(A)
    heapq.heapify(A)

    while len(A) > 1 and A[0] < k:
        first = heapq.heappop(A)
        second = heapq.heappop(A)
        sweetness = first + second * 2
        heapq.heappush(A, sweetness)

    return n - len(A) if A[0] >= k else -1
