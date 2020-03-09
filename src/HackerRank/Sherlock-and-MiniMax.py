"""
Sherlock and MiniMax
https://www.hackerrank.com/challenges/sherlock-and-minimax/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndMinimax function below.
def sherlockAndMinimax(arr, p, q):
    maximum = -1
    answer = 0
    ca = []
    arr.sort()

    # use only p, q, and mid = (a_i+a_(i+1)/2)
    for i in range(len(arr)-1):
        if (arr[i] + arr[i+1]) % 2 == 0:
            ca.append((arr[i] + arr[i+1]) // 2)
        else:
            ca.append((arr[i] + arr[i+1]) // 2)
            ca.append((arr[i] + arr[i+1]) // 2 + 1)
    
    ca.append(p)
    ca.append(q)
    
    ca.sort()

    # find minimum for each M
    for M in ca:
        if M >= p and M <= q:
            temp = findMinimum(arr, M)
            if maximum < temp:
                maximum = temp
                answer = M

    return(answer)

def findMinimum(arr, M):
    minimum = 2147483647
    for i in range(len(arr)):
        temp = abs(arr[i] - M)
        if minimum > temp:
            minimum = temp

    return minimum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    pq = input().split()

    p = int(pq[0])

    q = int(pq[1])

    result = sherlockAndMinimax(arr, p, q)

    fptr.write(str(result) + '\n')

    fptr.close()
