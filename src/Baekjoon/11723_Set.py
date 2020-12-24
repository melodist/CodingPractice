"""
https://www.acmicpc.net/problem/11723
Using set
"""
#1. Solution using set (3516ms)
import sys


input = sys.stdin.readline
m = int(input())
s = set()
g = (i for i in range(1, 21))
for _ in range(m):
    c = input().split()
    if c[0] == 'add':
        s.add(int(c[1]))
    elif c[0] == 'remove':
        if int(c[1]) in s:
            s.remove(int(c[1]))
    elif c[0] == 'check':
        if int(c[1]) in s:
            print(1)
        else:
            print(0)
    elif c[0] == 'toggle':
        if int(c[1]) in s:
            s.remove(int(c[1]))
        else:
            s.add(int(c[1]))
    elif c[0] == 'all':
        s = set(g)
    else:
        s.clear()

#2. Solution using dict and bit mask (5848ms)
import sys


input = sys.stdin.readline
m = int(input())
s = {k:0 for k in range(1, 21)}
for _ in range(m):
    c = input().split()
    if c[0] == 'add':
        s[int(c[1])] = 1
    elif c[0] == 'remove':
        s[int(c[1])] = 0
    elif c[0] == 'check':
        print(s[int(c[1])])
    elif c[0] == 'toggle':
        s[int(c[1])] = s[int(c[1])] ^ 1
    elif c[0] == 'all':
        s = {k:1 for k in range(1, 21)}
    else:
        s = {k:0 for k in range(1, 21)}
