"""
https://www.acmicpc.net/problem/12871
String Problem
"""
#1. My Solution (76ms)
s = input().strip()
t = input().strip()

print(1 if s * len(t) == t * len(s) else 0)
