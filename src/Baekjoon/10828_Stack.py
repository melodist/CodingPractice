"""
https://www.acmicpc.net/problem/10828
Using stack and optimization
"""
#1. My Solution
import sys

stack = []
answer = ''
for _ in range(int(input())):
    s = sys.stdin.readline().strip().split()
    if s[0] == 'push':
        stack.append(s[1])
        continue
    elif s[0] == 'pop':
        answer += stack.pop() if stack else '-1'
    elif s[0] == 'size':
        answer += str(len(stack))
    elif s[0] == 'empty':
        answer += '0'  if stack else '1'
    else:
        answer += stack[-1] if stack else'-1'
    answer += '\n'
    
print(answer)

#2. Other Solution
from sys import stdin

stack = []
next(stdin)
for line in stdin:
    command = line.split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if stack: print(stack.pop())
        else: print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if stack: print(0)
        else: print(1)
    elif command[0] == 'top':
        if stack: print(stack[-1])
        else: print(-1)
