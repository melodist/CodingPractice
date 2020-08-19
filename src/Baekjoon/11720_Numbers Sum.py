"""
https://www.acmicpc.net/problem/11720
"""
from functools import reduce


n = int(input())
print(reduce(lambda x, y: int(x) + int(y), input()))
