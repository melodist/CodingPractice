"""
https://www.acmicpc.net/problem/10989
Counting Sort
입력을 배열에 담으려고 할 경우 메모리 초과 -> 최대값이 10000을 넘지 않는 것을 이용
input()을 사용할 경우 시간 초과 -> sys.stdin.readline() 이용
"""
import sys

n = int(input())
counts = [0] * 10001

for i in range(n):
    num = int(sys.stdin.readline())
    counts[num] += 1
    
for i in range(1, len(counts)):
    if counts[i] != 0:
        for j in range(counts[i]):
            print(i)
