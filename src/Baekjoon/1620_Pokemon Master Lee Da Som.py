"""
https://www.acmicpc.net/problem/1620
Implementation Problem
"""
#1. My Solution (248ms)
import sys


input = sys.stdin.readline
n, m = map(int, input().split())
ntoi = {}
pokedex = [] 
for i in range(1, n+1):
    pokemon = input().strip()
    pokedex.append(pokemon)
    ntoi[pokemon] = i

for i in range(m):
    q = input().strip()
    if q.isdigit():
        print(pokedex[int(q)-1])
    else:
        print(ntoi[q])
