"""
https://www.acmicpc.net/problem/2750
O(n^2) Sort
1. Bubble Sort
- 1,2번째 원소를 비교하여 교환, ..., n-1, n번째 원소를 비교하여 교환 -> n번째 원소가 정렬됨
- 1,2번째 원소를 비교하여 교환, ..., n-2, n-1번째 원소를 비교하여 교환 -> n-2번째 원소가 정렬됨

2. Selection Sort
- 1번째 원소의 위치 k1를 찾아 k1번째 원소와 교환 -> 1번째 원소가 정렬됨
- 2번째 원소의 위치 k2를 찾아 k2번째 원소와 교환 -> 2번재 원소가 정렬됨
Bubble Sort에 비해 약 2배 정도 빠름
"""
# 1. Bubble Sort
n = int(input())
a = [int(input()) for i in range(n)]
for i in range(n-1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            
print(" ".join(map(str, a)))

# 2. Selection Sort
for i in range(n-1):
    cur = i
    for j in range(i+1, n):
        if a[cur] > a[j]:
            cur = j
    a[i], a[cur] = a[cur], a[i]
    print(a[i])

print(a[-1])
