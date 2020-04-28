"""
https://www.acmicpc.net/problem/1786
Using KMP.
1. Calculate Failure Function f for P
2. Matching T with P using f
"""
import sys
 
T = sys.stdin.readline().replace('\n', '')
P = sys.stdin.readline().replace('\n', '')
n = len(P)
m = len(T)

f = [0] * n
begin, matched = 1, 0
while begin + matched < n:
    if P[begin + matched] == P[matched]:
        matched += 1
        f[begin + matched - 1] = matched
    else:
        if matched == 0:
            begin += 1
        else:
            begin += matched - f[matched - 1]
            matched = f[matched - 1]

ans = []
cur, j = 0, 0
while cur <= m - n:
    if j < n and T[cur+j] == P[j]:
        j += 1
        if j == n:
            ans.append(str(cur+1))
    else:
        if j == 0:
            cur += 1 
        else:
            cur += j - f[j-1]
            j = f[j-1]

print(len(ans))    
if len(ans) != 0: print(' '.join(ans))
