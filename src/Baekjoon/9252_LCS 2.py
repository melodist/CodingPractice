"""
https://www.acmicpc.net/problem/9252
Longest Common Sequence (LCS) Problem
"""
#1. My Solution
s1 = input()
s2 = input()

prev = [''] * (len(s2)+1)
curr = [''] * (len(s2)+1)

for r in s1:
    for j, c in enumerate(s2, 1):
        if r == c:
            curr[j] = prev[j-1] + c
        else:
            curr[j] = prev[j] if len(prev[j]) > len(curr[j-1]) else curr[j-1]
            
    prev, curr = curr, prev

print(len(prev[-1]))
print(prev[-1])

#2. Other Solution
s1, s2 = input(), input()
d = [[] for _ in range(len(s2))]

for i in range(len(s1)):
    p = []
    for j in range(len(s2)):
        if len(d[j]) > len(p): p = d[j]
        elif s1[i] == s2[j] and len(d[j]) <= len(p): d[j] = p + [i]

ans = []
for i in d:
    if len(i) > len(ans):
        ans = i
print(len(ans))
print(''.join(map(lambda x:s1[x], ans)))
