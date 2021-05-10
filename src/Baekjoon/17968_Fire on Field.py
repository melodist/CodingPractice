"""
https://www.acmicpc.net/problem/17968
Brute Force로 해결. A[2]부터 A[n]까지 전부 구해야 함.
"""
def check(A, n, value):
    for k in range(1, n // 2 + 1):
        if value - A[n-k] == A[n-k] - A[n-2*k]:
            return False
    return True

n = int(input())
A = {0:1, 1:1}

for i in range(2, n+1):
    temp = 0
    flag = True
    while flag:
        temp += 1
        if check(A, i, temp):
            flag = False
    A[i] = temp
print(A[n])
    
