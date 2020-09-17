"""
https://www.acmicpc.net/problem/1918
Using stack
"""
#1. My Solution
s = input()
order = {'(' : 0, '*' : 2, '/': 2, '+' : 1, '-' : 1, ')' : 0}
stack = []
ans = ''

for c in s:
    if c.isalpha():
        ans += c
    else:
        if c == '(':
            stack.append(c)
        elif c == ')':
            while True:
                d = stack.pop()
                if d == '(':
                    break
                ans += d
        else:
        # Pop elements until stack[-1] is smaller than c
            while stack and order[c] <= order[stack[-1]]:
                ans += stack.pop()
            stack.append(c)    
print(ans+''.join(stack[::-1]))
