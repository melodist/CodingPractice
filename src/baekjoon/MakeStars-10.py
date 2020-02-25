""" 2447번: 별 찍기 - 10
https://www.acmicpc.net/problem/2447

Divide-and-Conquer 이용하여 해결
분할, 정복, 합치기
"""
def make_stars(n):
    matrix=[]
    for i in range(3*len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len (n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return(list(matrix))

n = int(input())
star = ['***','* *', '***']
k = 0

while n != 3:
    n = int(n / 3)
    k += 1

for i in range(k):
    star = make_stars(star)
for i in star:
    print(i)
