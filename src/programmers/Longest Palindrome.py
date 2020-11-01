"""
https://programmers.co.kr/learn/courses/30/lessons/12904?language=python3
Using recursion
"""
#1. My Solution
import sys


def isPalindrome(s, i, j):
    if i == j or i > j:
        return True
    
    if s[i] == s[j]:
        return isPalindrome(s, i+1, j-1)
    else:
        return False

def solution(s):
    sys.setrecursionlimit(10**8)
    answer = 0
    n = len(s)
    for a in range(n):
        for b in range(n-1, a-1, -1):
            if isPalindrome(s, a, b):
                answer = max(answer, b-a+1)
                break
            
    return answer
