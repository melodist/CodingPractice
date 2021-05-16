"""
https://www.acmicpc.net/problem/17822
Implementation Problem
"""
#1. My Solution (268ms)
import sys


input = sys.stdin.readline
disc = []
N, M, T = map(int, input().split())

# disc input
for _ in range(N):
    disc.append([*map(int, input().split())])
    
# rotate discs    
for _ in range(T):
    x, d, k = map(int, input().split())
    
    # Find rotation direction
    rot =  1 if d == 0 else -1
        
    for i in range(N):
        if (i+1) % x == 0:
            temp = [0] * M
            for j in range(M):
                temp[(j+k*rot) % M] = disc[i][j]
            disc[i] = temp
            
    # find answer
    check = [[True] * M for _ in range(N)]
    check_cnt = 0
    for i in range(N):
        for j in range(M):
            # vertical check
            if disc[i][j] > 0:
                if i > 0 and disc[i][j] == disc[i-1][j]:
                    check[i][j] = False
                    check_cnt += 1
                if i < N-1 and disc[i][j] == disc[i+1][j]:
                    check[i][j] = False
                    check_cnt += 1
                
                # horizontal check
                if disc[i][j] == disc[i][(j+1) % M]:
                    check[i][j] = False
                    check_cnt += 1
                if disc[i][j] == disc[i][(j-1) % M]:
                    check[i][j] = False            
                    check_cnt += 1
                
    # print("After rotate")
    # print(disc, check_cnt)
    if check_cnt:
        for i in range(N):
            for j in range(M):
                if not check[i][j]:
                    disc[i][j] = 0
    else:
        disc_cnt = 0
        disc_sum = 0
        for i in range(N):
            for j in range(M):
                if disc[i][j]:
                    disc_cnt += 1
                    disc_sum += disc[i][j]
        
        if disc_cnt > 0:
            disc_avg = disc_sum / disc_cnt
            # print(disc_cnt, disc_sum, disc_avg)
            for i in range(N):
                for j in range(M):
                    if disc[i][j] > 0:
                        if disc[i][j] < disc_avg:
                            disc[i][j] += 1
                        elif disc[i][j] > disc_avg:
                            disc[i][j] -= 1
                            
    # print(disc)
                        
print(sum([sum(disc[r]) for r in range(N)]))

#2. Other Solution (120ms)
MIS = lambda: map(int, input().split())

# left, down check
def erase():
    P = []
    for i in range(N):
        for j in range(M):
            if disks[i][j] == disks[i][j-1] != 0: P.append((i,j,i,j-1))
    for i in range(N-1):
        for j in range(M):
            if disks[i][j] == disks[i+1][j] != 0: P.append((i,j,i+1,j))
    return P


def average():
    num = N * M - sum(row.count(0) for row in disks)
    if num == 0: return
    avg = sum(map(sum, disks)) / num

    for y in range(N):
        for x in range(M):
            if disks[y][x] == 0: continue
            if disks[y][x] < avg: disks[y][x]+=1
            elif disks[y][x] > avg: disks[y][x]-=1


N, M, T = MIS()
disks = [list(MIS()) for _ in range(N)]

for _ in range(T):
    x, d, k = MIS()
    if d == 1: k = M - k  # k의 범위가 M을 넘지 않고, d를 사용하지 않는다.

    # rotate
    for c in range(x - 1, N, x):
        disks[c] = disks[c][M - k:] + disks[c][:M - k]

    # adj
    p = erase()
    if p:
        for i1,j1,i2,j2 in p: disks[i1][j1] = disks[i2][j2] = 0
    else:
        average()
print(sum(map(sum, disks)))
