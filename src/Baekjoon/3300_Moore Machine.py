"""
https://www.acmicpc.net/problem/3300
Using Regular Expression
Replace _ to all capitals and find the number meets the condition
"""
import re


for _ in range(int(input())):
    moore = input().strip()
    output = input().strip()

    answer = []
    for i in range(ord('Z') - ord('A') + 1):
        c = chr(ord('A') + i)
        p = '^(' + moore.replace('_', c) + ')$'
        r = re.compile(p)
        if r.match(output):
            answer.append(c)
            
    if len(answer) > 1:
        print('_')
    elif len(answer) == 0:
        print('!')
    else:
        print(answer[0])
