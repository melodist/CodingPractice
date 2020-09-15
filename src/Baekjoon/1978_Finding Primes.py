"""
https://www.acmicpc.net/problem/1978
Using Sieve of Eratosthenes
"""
MAX = 1001
n = int(input())
arr = [*map(int, input().split())]
isprime = [True] * MAX
isprime[0] = False
isprime[1] = False

for i in range(2, MAX):
    if not isprime: continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            isprime[i] = False
    for k in range(i*i, MAX, i):
        isprime[k] = False

ans = 0            
for a in arr:
    if isprime[a]: ans += 1
    
print(ans)
