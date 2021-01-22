"""
https://www.acmicpc.net/problem/17626
Using dynamic programming
Maximum value is 4
"""
#1. My Solution (108ms)
n = int(input())
min_sum = 4 
for a in range(int(n**0.5), int((n//4)**0.5), -1):
    if a*a == n:
        min_sum = 1
        break
    else:
        temp = n - a*a
        for b in range(int(temp**0.5), int((temp//3)**0.5), -1):
            if a*a + b*b == n:
                min_sum = min(min_sum, 2)
                continue
            else:
                temp = n - a*a - b*b
                for c in range(int(temp**0.5), int((temp//2)**0.5), -1):
                    if n == a*a + b*b + c*c:
                        min_sum = min(min_sum, 3)
                
print(min_sum)

#2. Other Solution (76ms)
n = int(input())

max_num = int(n**(1/2))
first_step = {i**2 for i in range(1, max_num + 1)}
second_step = {i**2 + j**2 for i in range(max_num + 1) for j in range(i, max_num + 1)}

if n in first_step:
    print(1)
elif n in second_step:
    print(2)
else:
    for first in first_step:
        if n - first in second_step:
            print(3)
            break
    else:
        print(4)
