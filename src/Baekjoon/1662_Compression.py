"""

Using recursion and stack
"""
#1. My Solution
s = input()
stack = []
size = 0
temp = ''
for c in s:
    if c.isdigit():
        size += 1
        temp = c
    elif c == '(':
        stack.append((temp, size - 1))
        size = 0
    else:
        front, size_front = stack.pop()
        size = size_front + int(front) * size

print(size)
