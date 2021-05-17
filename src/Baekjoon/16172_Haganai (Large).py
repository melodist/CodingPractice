"""
https://www.acmicpc.net/problem/16172
Using KMP
"""
#1. My Solution (284ms)
# Find keyword without numbers
s1 = input()
s2 = ''
for c in s1:
    if ord(c) > ord('9') or ord(c) < ord('0'):
        s2 += c
        
s3 = input()
flag = 0

# Find Pi Array which contains maximum length with prefix == suffix for each substring s[:i+1]
# ex). s = abbab, pi[4] = 2 (s[0] == s[3], s[1] == s[4])
n, m = len(s2), len(s3)
j = 0
pi = [0] * m
for i in range(1, m):
    while j > 0 and s3[i] != s3[j]:
        j = pi[j-1]
    if s3[i] == s3[j]:
        j += 1
        pi[i] = j

# KMP Algorithm
j = 0
for i in range(n):
    while j > 0 and s2[i] != s3[j]:
        j = pi[j-1]
    if s2[i] == s3[j]:
        if j == m-1:
            flag = 1
            break
        else:
            j += 1
    
print(flag)
