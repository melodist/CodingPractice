"""
Using reduce
"""
from functools import reduce

s = input()
flag = True if s[0] == '-' else False

major = s[:s.find('.')] if not flag else s[1:s.find('.')]
minor = s[s.find('.')+1:]

front = reduce(lambda x, y: 10 * int(x) + int(y), list(major))
rear = reduce(lambda x, y: float(x) / 10 + float(y), list(minor[::-1]))

print(-(front+rear/10) if flag else front+rear/10)
