"""
https://www.acmicpc.net/problem/14888
Use array for visited permutation
"""
#1. Brute Force
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


#2. BackTracking
n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

def backtrack(value, l, plus, minus, times, div):
    global ans_min, ans_max
    if l == n - 1:
        if ans_min > value:
            ans_min = value
        if ans_max < value:
            ans_max = value
        return
    
    if plus:
        backtrack(value + nums[l+1], l+1, plus-1, minus, times, div)
        
    if minus:
        backtrack(value - nums[l+1], l+1, plus, minus-1, times, div)
        
    if times:
        backtrack(value * nums[l+1], l+1, plus, minus, times-1, div)
        
    if div:
        if value < 0:
            backtrack(- ((-value) // nums[l+1]), l+1, plus, minus, times, div-1)
        else:
            backtrack(value // nums[l+1], l+1, plus, minus, times, div-1)
            
ans_min = 10E10
ans_max = -10E10

backtrack(nums[0], 0, *operators)

print(ans_max, ans_min, sep='\n')
