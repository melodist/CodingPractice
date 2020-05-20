"""
https://www.acmicpc.net/problem/14501
"""
def generate(t, p):
    temp = p
    for i in range(t, N):
        if i+T[i] <= N:
            temp = max(temp, generate(i+T[i], p+P[i]))
        
    return temp

N = int(input())

T = [0] * N
P = [0] * N

for i in range(N):
    T[i], P[i] = map(int, input().split())
    
print(generate(0, 0))
