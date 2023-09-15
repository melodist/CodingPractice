"""
https://www.acmicpc.net/problem/1427
Using Counting Sort.
"""
n = int(input())

count = [0] * 10

while n != 0:
    count[n % 10] += 1
    n //= 10

i, digit = 0, 0
temp = 0
while i < 10:
    if count[i] > 0:
        temp += i * (10 ** digit)
        count[i] -= 1
        digit += 1
    else:
        i += 1
        
print(temp)
