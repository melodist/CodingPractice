"""
https://www.acmicpc.net/problem/2798
"""
import itertools

n, m = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0

for a, b, c in itertools.combinations(nums, 3):
    temp = a + b + c
    if m - answer > m - temp and m >= temp:
        answer = temp
        
print(answer)
