"""
https://programmers.co.kr/learn/courses/30/lessons/12977
Using
"""
#1. My Solution
def solution(nums):
    n = len(nums)
    nums = sorted(nums)
    max_value = nums[-1] + nums[-2] + nums[-3]
    is_prime = [True] * (max_value + 1)
    
    for p in range(2, int((max_value)**0.5) + 1):
        if not is_prime[p]: continue
        for i in range(p*2, max_value+1, p):
            is_prime[i] = False
    
    answer = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                temp = nums[i] + nums[j] + nums[k]
                if is_prime[temp]: answer += 1

    return answer

#2. Other Solution
from itertools import combinations
def prime_number(x):
    answer = 0
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            answer+=1
    return 1 if answer==1 else 0

def solution(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums,3)])
