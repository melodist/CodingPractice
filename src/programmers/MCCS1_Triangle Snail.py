"""
https://programmers.co.kr/learn/courses/30/lessons/68645
"""
#1. My Solution
from functools import reduce


def solution(n):
    triangle = [[0] * i for i in range(1, n+1)]
    total = n * (n+1) // 2
    left = 0; right = 0; up = 0; down = n; cnt = 0
    i = 0; j = 0
    while cnt < total:
        for i in range(up, down):
            triangle[i][j] = cnt+1
            cnt += 1
        left += 1
        down -= 1


        for j in range(left, n - right):
            triangle[i][j] = cnt+1
            cnt += 1
        up += 1        
        right += 1 
        i -= 1
        j -= 1

        while i >= up:
            triangle[i][j] = cnt+1
            cnt += 1
            i -= 1
            j -= 1

        j = left
        up += 1
        right += 1

    return reduce(lambda x, y: x + y, triangle)
    
#2. Other Solution
def solution(n):
    mat = [[0 for col in range(row + 1)] for row in range(n)]
    count = 0
    idx = [-1,0]
    while n > 0:
        for i in range(n):
            count += 1
            idx[0] += 1
            mat[idx[0]][idx[1]] = count
        n -= 1
        if n <= 0:
            break
        for i in range(n):
            count += 1
            idx[1] += 1
            mat[idx[0]][idx[1]] = count
        n -= 1
        if n <= 0:
            break
        for i in range(n):
            count += 1
            idx[0] -= 1
            idx[1] -= 1
            mat[idx[0]][idx[1]] = count
        n -= 1
    answer = []
    for row in mat:
        answer += row
    return answer
