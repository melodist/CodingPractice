"""
https://programmers.co.kr/learn/courses/30/lessons/62049
비트 논리 연산자 : & (and) / | (or) /  ^ (xor) / ~ (not)
"""
def solution(n):
    fold = 0
    arr = [fold]

    for i in range(n - 1):
        arr = arr + [fold] + [bit ^ 1 for bit in arr[::-1]]

    return arr
