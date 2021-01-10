"""
https://www.acmicpc.net/problem/17219
Using hash
"""
#1. My Solution (264ms)
import sys


input = sys.stdin.readline
n, m = map(int, input().split())
pwd = {}
for _ in range(n):
    i, p = input().split()
    pwd[i] = p
    
for _ in range(m):
    print(pwd[input().strip()])
