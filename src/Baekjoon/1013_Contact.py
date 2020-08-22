"""
https://www.acmicpc.net/problem/1013
Using Regular Expression
"""
import re


p = re.compile('^(100+1+|01)+$') # ^ means start with this expression, $ means end with this expression
for _ in range(int(input())):
    print('YES' if p.match(input()) else 'NO')
