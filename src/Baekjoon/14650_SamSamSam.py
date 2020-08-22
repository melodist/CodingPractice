"""
https://www.acmicpc.net/problem/14650
Using regular expression and product
In f-string, {{ and }} can escape { and }
"""
import re
from itertools import product

n = int(input())
arr = [('0', '1', '2')] * n
answer = 0

p = re.compile(f'^[1-2][0-2]{{{str(n-1)}}}$')
for i in product(*arr):
    num = ''.join(i)
    if p.match(num) and int(num) % 3 == 0:
        answer += 1
        
print(answer)
