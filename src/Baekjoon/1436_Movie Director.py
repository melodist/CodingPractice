"""
https://www.acmicpc.net/problem/1436
Brute Force
"""
#1. My Solution
n = int(input())
temp = 666
count = 0
while count < n:
    if str(temp).count('666') > 0:
        count += 1
    temp += 1
    
print(temp - 1)

#2. Other Solution
print([i for i in range(9**7)if"666"in str(i)][int(input())-1])
