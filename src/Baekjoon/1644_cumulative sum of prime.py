"""
https://www.acmicpc.net/problem/1644
Using two pointer approach and sieve of Eratosthenes
"""
#1. My Solution
n = int(input())
check = [False] * (n+1)
primes = []

# Sieve of Eratosthenes - O(nlog^2n)
for i in range(2, n+1):
    if not check[i]:
        primes.append(i)
        for j in range(i*i, n+1, i):
            check[j] = True

m = len(primes)
arr = [0] * (m + 1)
for i, x in enumerate(primes, 1):
    arr[i] = arr[i-1] + x

# Two pointer approach
left = 0; right = 1
answer = 0
while right <= m:
    if arr[right] - arr[left] == n:
        answer += 1
        left += 1
    elif arr[right] - arr[left] > n:
        left += 1
    else:
        right += 1
        
print(answer)

#2. Other Solution
def primes(n):
    result = [False,False] + [True]*(n-1)
    for i in range(2, int(n**0.5+1.5)):
        if result[i]:
            result[2*i::i] = [False]*((n-i)//i)
    return [x for x in range(n+1) if result[x]]

n = int(input())
cnt = 0
prime = primes(n)
length = len(prime)
L = 0
R = 0
S = 0
if n==0: print(0)
else:
    while True:
        if S >= n:
            S -= prime[L]
            L += 1
        elif R>= length:break
        else:
            S += prime[R]
            R+=1
        if S == n: cnt += 1
    print(cnt)
