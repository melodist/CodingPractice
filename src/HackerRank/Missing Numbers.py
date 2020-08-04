"""
https://www.hackerrank.com/challenges/missing-numbers/problem
"""
#1. My Solution using Hashmap
from collections import defaultdict


def missingNumbers(arr, brr):
    freq = defaultdict(int)
    answer = []

    for b in brr:
        freq[b] += 1

    for a in arr:
        freq[a] -= 1

    for f in freq:
        if freq[f] != 0:
            answer.append(f)

    return sorted(answer)
    
#2. Other Solutuion using Array
def missingNumbers(arr, brr):
    A = [0] * 10001
    B = [0] * 10001
    answer = []

    for b in brr:
        B[b] += 1

    for a in arr:
        A[a] += 1

    for i in range(1, 10001):
        if B[i] > A[i]:
            answer.append(i)

    return answer
