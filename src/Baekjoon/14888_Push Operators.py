"""
https://www.acmicpc.net/problem/14888
Use array for visited permutation
"""
from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
ops = ''.join([str(i) * operators[i] for i in range(4)])

def calculate(op, a, b):
    if op == '0':
        return a + b
    elif op == '1':
        return a - b
    elif op == '2':
        return a * b
    else:
        return a // b if a > 0 else - ((-a) // b)

ans_min, ans_max = 10E11, -10E11
visited = set()

for p in permutations(ops):
    if p in visited:
        continue

    temp = nums[0]
    for i, op in enumerate(p):
        temp = calculate(op, temp, nums[i+1])

    if ans_min > temp:
        ans_min = temp
    if ans_max < temp:
        ans_max = temp
        
    visited.add(p)
    
print(ans_max, ans_min, sep='\n')
