"""
https://www.acmicpc.net/problem/2220
Heap sort 시 heap에서 최상위 값을 제거하면 남은 부분이 heap 형태를 유지함.
따라서, swap 회수가 가장 많도록 heap을 만들면 heap sort 시 swap 회수가 최대가 됨.
1. 이전 최대 힙에 다음 값을 더하고 1과 자리를 교환
2. 더한 값이 최상위로 오도록 swap
"""
n = int(input())
heap = [0, 1]

def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]
 
for i in range(2, n+1):
    heap.append(i)
    # swap the value with 1 (i -> i / 1 -> i-1)
    swap(heap, i, i-1)
    j = i-1
    # create max heap
    while j != 1:
        swap(heap, j, j//2)
        j = j//2

for i in heap[1:]:
    print(i, end = ' ')
