"""
https://www.acmicpc.net/problem/11444
Using divide and conquer
Matrix Multiplication
"""
#1. My Soltuion (68ms)
def matrixMul(a, b):
    print(a, b)
    ret = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ret[i][j] += a[i][k] * b[k][j]
                ret[i][j] %= MOD
                
    return ret

def func(n):
    init = [[1, 1], [1, 0]]
    if n == 1:
	    return init
    if n % 2:  # n 홀수
        tmp = func(n - 1)
        return matrixMul(init, tmp)
    else: # n 짝수
        tmp = func(n // 2)
        return matrixMul(tmp, tmp)

MOD = 1000000007
n = int(input())

ret = func(n)
print(ret[1][0])
