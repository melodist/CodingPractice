"""
https://www.acmicpc.net/problem/17609
Using two pointer approach
"""
#1. My Solution
import sys


def ispalindrome(l, r, s, flag):
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        elif flag == 0:
            return 1 if ispalindrome(l, r-1, s, 1) == 0 or ispalindrome(l+1, r, s, 1) == 0 else 2
        else:
            return 2
            
    return 0

input = sys.stdin.readline
for _ in range(int(input().strip())):
    s = input().strip()
    print(ispalindrome(0, len(s)-1, s, 0))
    
#2. Other Solution
def is_palindrome(s):
    if s == s[::-1]:
        return True


def solution(s):
    if is_palindrome(s):
        return 0
    
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            if is_palindrome(s[i + 1: j + 1]):
                return 1
            elif is_palindrome(s[i: j]):
                return 1
            else:
                return 2
        i += 1
        j -= 1
        

n = int(input())
for _ in range(n):
    s = input().strip()
    print(solution(s))
