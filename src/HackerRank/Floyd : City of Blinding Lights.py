"""
https://www.hackerrank.com/challenges/floyd-city-of-blinding-lights/problem
Using Floyd-Warshall Algorithm and Optimization
Using Pypy 3 because of timeout in Python 3
"""
n, m=map(int, input().split())
MAX = 400**2  # Optimization 1: Using small MAX
dist=[MAX]*(n+1)**2  # Optimization 2: Using 1D array

for _ in range(m):
    i,j,w=map(int,input().split())
    dist[i*(n+1)+j]=w 
for i in range(1,n+1):
    dist[i*(n+1)+i]=0

for k in range(1,n+1):
    for i in range(1,n+1):
        if dist[i*(n+1)+k] == MAX: continue  # Optimization 3: Skip for unnecessary cases
        for j in range(1,n+1):
            if dist[k*(n+1)+j] == MAX: continue
            dist[i*(n+1)+j]=min(dist[i*(n+1)+j],
            dist[i*(n+1)+k]+dist[k*(n+1)+j])

q=int(input())

for _ in range(q):
    i, j=map(int, input().split())
    print(dist[i*(n+1)+j] if dist[i*(n+1)+j]!=MAX else -1)
