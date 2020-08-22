"""
https://www.acmicpc.net/problem/9342
Using Regular Expression
Caution to '\n'
Using strip() to get rid of whitespace
"""
import re


r = '^[A-F]?A+F+C+[A-F]?$'
p = re.compile(r)
for i in range(int(input())):
    print('Infected!' if p.match(input().strip()) else 'Good')
