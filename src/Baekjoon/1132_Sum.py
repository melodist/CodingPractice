"""
Using Greedy Algorithm
Note that there are no number starts with zero
"""
#1. Failed Solution
#Only remove the case with single character. (ex. A, B, C, ...)
#8
#A
#BB
#CCC
#DDDD
#EEEEE
#FFFGGG
#HHHHHHH
#IJJJJJJJ
# >> 107393220 (answer : 107393020)
import sys
from collections import defaultdict, deque


n = int(input())
ones = set()
dic = defaultdict(int)
for i in range(n):
    s = sys.stdin.readline().strip()
    if len(s) == 1:
        ones.add(s)
    temp = 1
    for c in s[::-1]:
        dic[c] += temp
        temp *= 10

dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
print(dic)

q = deque([i for i in range(10)])
answer = 0
chars = 10
for c, v in dic:
    if chars == len(ones) + 1 and c not in ones:
        value = q.popleft()
    else:
        value = q.pop()
    answer += v * value
    print(c, value)
    
    if c in ones:
        ones.remove(c)
    chars -= 1
    
print(answer)

#2. Accepted Solution
# Store the first character on each number and this couldn't be zero
import sys
from collections import defaultdict, deque


n = int(input())
starts = set()
dic = defaultdict(int)
for i in range(n):
    s = sys.stdin.readline().strip()
    temp = 1
    for c in s[::-1]:
        dic[c] += temp
        temp *= 10
    starts.add(s[0])

dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
# print(dic)

q = deque([i for i in range(10)])
answer = 0
chars = 10
for c, v in dic:
    if chars == len(starts) + 1 and c not in starts:
        value = q.popleft()
    else:
        value = q.pop()
    answer += v * value
    # print(c, value)
    
    if c in starts:
        starts.remove(c)
    chars -= 1
    
print(answer)

