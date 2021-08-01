"""
https://www.acmicpc.net/problem/7512
Using Sliding Window
"""
#1. My Solution (4624ms)
import sys
from itertools import accumulate


def solve():
    ni = [0] * 11

    # Make (m+1) windows for each value n_i
    subsums = []
    subsums.append(prime)

    for i in range(1, m+1):
        subsums.append([])
        for j in range(nPrime - nn[i-1] + 1):
            temp = accPrime[j + nn[i-1]] - accPrime[j]
            if temp < MAX:
                subsums[i].append(temp)
            else:
                break

    p = 0
    flag = False

    while not flag:
        # Find maximum value of each window
        for i in range(m+1):
            p = max(p, subsums[i][ni[i]])

        # Find index for equal or larger value than p 
        for j in range(m+1):
            while subsums[j][ni[j]] < p:
                ni[j] += 1

        # Check all values are same
        flag = True
        for k in range(m+1):
            if subsums[k][ni[k]] != p:
                flag = False

    return p


input = sys.stdin.readline
MAX = 10_000_000

# Find prime
isPrime = [True] * (MAX + 1)

for i in range(2, int(MAX ** 0.5) + 1):
    if isPrime[i]:
        for j in range(2 * i, MAX + 1, i):
            isPrime[j] = False

prime = []
for i in range(2, MAX + 1):
    if isPrime[i]:
        prime.append(i)

accPrime = [0] + list(accumulate(prime))
nPrime = len(prime)

c = int(input())
for x in range(c):
    m = int(input())
    nn = [*map(int, input().split())]

    ans = solve()

    print(f"Scenario {x + 1}: ")
    print(ans)
    print()
