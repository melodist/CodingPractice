"""
https://www.hackerrank.com/challenges/maximum-element/problem
"""
stack = []
stack_max = []
m = 0

for i in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 1:
        stack.append(q[1])
        if m <= q[1]:
            stack_max.append(q[1])
            m = q[1]
    elif q[0] == 2:
        temp = stack.pop()
        if stack:
            if temp == m:
                stack_max.pop()
                m = stack_max[-1]
        else:
            m = 0

    else:
        print(m)
