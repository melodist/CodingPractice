"""
https://www.acmicpc.net/problem/16916
Using KMP Algorithm
"""
#1.My Solution (948ms)
import sys


input = sys.stdin.readline
s1 = input().strip()
s2 = input().strip()

n, m = len(s1), len(s2)
# Find Pi
pi = [0] * m
j = 0
for i in range(1, m):
    while j > 0 and s2[i] != s2[j]:
        j = pi[j-1]
    if s2[i] == s2[j]:
        j += 1
        pi[i] = j

# KMP Algorithm
j, k = 0, 0
flag = 0
for i in range(n):
    while j > 0 and s1[i] != s2[j]:
        j = pi[j-1]
        
    if s1[i] == s2[j]:
        if j == m-1:
            flag = 1
            break
        else:
            j += 1
            
print(flag)
