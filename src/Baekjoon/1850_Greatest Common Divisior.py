"""
https://www.acmicpc.net/problem/1850
Using Euclidean Algorithm
"""
#1. My Solution (952ms)
a, b = map(int, input().split())
if a < b:
    a, b = b, a

while b > 0:
    r = a % b
    a = b
    b = r
    
ans = ''
for i in range(a): 
    ans += '1' # Too much Time
print(ans)

#2. Other Solution (60ms)
a,b=map(int,input().split())
while b: a,b=b,a%b
print('1'*a)
