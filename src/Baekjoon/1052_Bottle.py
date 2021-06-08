"""
https://www.acmicpc.net/problem/1052
Using bit mask
"""
#1. My Solution (4380ms)
n, k = map(int, input().split())
ans = 0
while True:
    if bin(n+ans)[2:].count('1') > k:
        ans += 1
    else:
        break
    
print(ans)

#2. Other Solution (52ms)
# 가장 뒤쪽의 1에 1을 더하는 방식으로 1의 개수를 줄일 수 있다
n,k=map(int,input().split())
c=0
while bin(n).count('1')>k:
 a=2**(bin(n)[::-1].index('1'))
 c+=a
 n+=a
print(c)
