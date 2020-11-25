"""
https://www.acmicpc.net/problem/1043
Using graph theory
"""
#1. My Solution (80ms)
import sys


input = sys.stdin.readline
n, m = map(int, input().split())
truth = set([*map(int, input().split())][1:])
ans = 0
parties = []

for _ in range(m):
    party = tuple(map(int, input().split()))
    parties.append(party)

for _ in range(m):
    for party in parties:
        for p in party[1:]:
            if p in truth:
                truth = truth.union(set(party[1:]))
                break

for party in parties:
    ans += 1
    for p in party[1:]:
        if p in truth:
            ans -= 1
            break
    
print(ans)

#2. Other Solution (56ms)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

k = map(int, input().split())
num = next(k)  # returns the next item from iterator, num == k[0]
fact = list(k)  # list(k[1:])
counted = set(fact)
linked = []
for _ in range(m):
    k = map(int, input().split())
    num = next(k)
    linked.append(set(k))
while fact and linked:
    i = fact.pop()
    new_linked = []
    for k in linked:
        if i in k:
            fact += list(k.difference(counted))
        else:
            new_linked.append(k)
    linked = new_linked

print(len(linked))
