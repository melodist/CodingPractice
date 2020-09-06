"""
https://www.acmicpc.net/problem/1747
Find palindrome and prime from n and increase n
Using Dynamic Programming to store palindromes
"""
import math


def is_palindrome(s, dp):
    if len(s) < 2:
        return True
    
    if s[0] == s[-1]:
        substr = s[1:-1]
        if substr in dp or is_palindrome(substr, dp):
            dp.add(substr)
            return True
        else:
            return False
    else:
        return False


def is_prime(n):
    if n < 2:
        return False
        
    end = int(n ** 0.5)
    for i in range(2, end+1):
        if n % i == 0:
            return False
        
    return True
    
    
n = int(input())
dp = set()

answer = n
while True:
    if is_palindrome(str(answer), dp) and is_prime(answer):
        print(answer)
        break
    answer += 1
