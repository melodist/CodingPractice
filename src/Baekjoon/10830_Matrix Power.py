"""
https://www.acmicpc.net/problem/10830
Using Divide and Conquer
Note that elements bigger than 1000 should be expressed in x % 1000
"""
#1. My Solution
import sys


def matrix_mul(arr1, arr2):
    n = len(arr1)
    if arr2 == 1:
        return arr1
        
    assert n == len(arr2)
    
    arr2_t = [list(row) for row in zip(*arr2)]
    
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = sum([x * y for x, y in zip(arr1[i], arr2_t[j])]) % 1000
        
    return temp
    
def divide(arr, b):
    if b == 0:
        return 1
    if b == 1:
        return [[x % 1000 for x in row] for row in arr]  # Though b == 1, arr should be expressed in x % 1000
        
    q, r = divmod(b, 2)
    
    arr_q = divide(arr, q)
    
    return matrix_mul(matrix_mul(arr_q, arr_q), divide(arr, r))
    
sys.setrecursionlimit(10**5) 
n, b = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]

[print(' '.join(map(str, row))) for row in divide(arr, b)]
