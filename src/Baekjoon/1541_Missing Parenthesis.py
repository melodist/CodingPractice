"""
https://www.acmicpc.net/problem/1541
Math Problem
"""
#1. My Solution (64ms)
s = input()
s += '\0'

ans = 0
temp = ''
minus = False

for c in s:
    if c == '-' or c == '+' or c == '\0':
        if minus:
            ans -= int(temp)
        else:
            ans += int(temp)
        temp = ''
        
        if c == '-':
            minus = True
    else:
        temp += c
        
print(ans)

#2. Other Solution (52ms)
# Calculate addition first
e = [sum(map(int, x.split('+'))) for x in input().split('-')]
print(e[0]-sum(e[1:]))
