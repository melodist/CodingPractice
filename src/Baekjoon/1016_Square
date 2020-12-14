"""
https://www.acmicpc.net/problem/1016
Using Sieve of Eratosthenes
"""
#1. My Solution (692ms)
v_min, v_max = map(int, input().split())
lim = int(v_max**0.5)
visited = [False] * (lim+1)
primes = []
ans = set()

for i in range(2, lim+1):
    if visited[i]:
        continue
    primes.append(i)
    for j in range(2*i, lim+1, i):
        visited[j] = True
        
for i in primes:
    a = i*i
    if v_min % a == 0:
        pivot = v_min
    else:
        pivot = (v_min // a + 1) * a

    for j in range(pivot, v_max+1, a):
        ans.add(j)

print(v_max - v_min - len(ans) + 1)

#2. Other Solution (172ms)
def prime(n):
    if n < 2:
        return []
    n += 1
    save = [1] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if save[i // 2]:
            k = i * i
            save[k // 2::i] = [0] * ((n - k - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if save[i]]

def list_ver():
    n, m = [int(i) for i in input().split()]
    a = int((m+1)**0.5)
    x = [1]*(m-n+1)
    for p in prime(a):
        div = p**2
        u, v = (n-1)//div+1, m//div + 1
        x[u*div-n::div] = [0]*(v-u)
    return sum(x)

print(list_ver())
