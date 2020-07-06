"""
https://www.hackerrank.com/challenges/qheap1/problem
"""
#1. My Solution
def insert(li, idx):
    parent = idx // 2
    while parent and li[parent] > li[idx]:
        li[parent], li[idx] = li[idx], li[parent]
        idx = parent
        parent //= 2
    
def delete(li, idx):
    l = idx * 2
    r = l + 1
    n = len(li) - 1

    s_idx = idx
    if l <= n and r <= n:
        small = l if li[l] < li[r] else r
    elif l <= n:
        small = l
    else:
        small = 0

    if small and li[small] < li[idx]:
        s_idx = small

    if s_idx != idx:
        li[idx], li[s_idx] = li[s_idx], li[idx]
        return delete(li, s_idx)

heap = [0]
for i in range(int(input())):
    coms = input().split()
    if coms[0] == '1':
        heap.append(int(coms[1]))
        insert(heap, len(heap) - 1)
    elif coms[0] == '2':
        heap.remove(int(coms[1]))
        delete(heap, 1)
    else:
        print(heap[1])


#2. Other Solution
from heapq import heappush, heappop

if __name__ == '__main__':
    heap, setq = [], set()
    PUSH, DELETE, PRINT = "1", "2", "3"

    for _ in range(int(input())):
        t = input().split()
        if t[0] == PUSH:
            v = int(t[1])
            heappush(heap, v)
            setq.add(v)

        elif t[0] == DELETE:
            v = int(t[1])
            setq.remove(v)
            while len(heap) > 0 and heap[0] not in setq:
                heappop(heap)
        else:
            print(heap[0])
