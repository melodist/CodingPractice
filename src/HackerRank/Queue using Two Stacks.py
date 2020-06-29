"""
https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
"""
s1 = []
s2 = []
front_s1 = 0
front_s2 = 0
for i in range(int(input())):
    codes = input().split()
    if codes[0] == '1':
        if front_s1 == 0:
            front_s1 = codes[1]
        s1.append(codes[1])
    elif codes[0] == '2':
        if not s2:
            while s1:
                s2.append(s1.pop())
            front_s1 = 0
        s2.pop()
        front_s2 = s2[-1] if s2 else 0
    else:
        print(front_s2 if front_s2 != 0 else front_s1)
