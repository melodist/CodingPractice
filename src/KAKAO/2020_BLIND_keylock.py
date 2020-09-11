"""
https://programmers.co.kr/learn/courses/30/lessons/60059
Implementation Problem
Using numpy for 2D array
"""
#1. My Solution
import numpy as np


def rot_90(arr):
    n = len(arr)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = arr[n-1-j][i]

    return ans

def match(key, lock, m, n, i, j):
    key_90 = rot_90(key)
    key_180 = rot_90(key_90)
    key_270 = rot_90(key_180)
    
    for k in (key, key_90, key_180, key_270):
        temp = lock.copy()
        temp[i:i+m, j:j+m] += k
        temp_cen = temp[m-1:-m+1, m-1:-m+1]
        if np.all(temp_cen == 1):
            return True
        
    return False

def solution(key, lock):
    m, n = len(key), len(lock)
    key = np.array(key); lock = np.array(lock)
    lock_padd = [[0] * (n+(m-1)*2) for _ in range(n+(m-1)*2)]
    for i in range(n):
        lock_padd[i+m-1][m-1:-m+1] = lock[i]

    lock_padd = np.array(lock_padd)
    for i in range(m+n-1):
        for j in range(m+n-1):
            if match(key, lock_padd, m, n, i, j):
                return True

    return False

#2. Former Solution
import numpy as np

def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    # [ [0] * N ] * N 으로 작성할 경우 모든 행의 값이 같게 됨.

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret


def rotate_180(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N-1-r][N-1-c] = m[r][c]
    return ret


def rotate_270(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N-1-c][r] = m[r][c]
    return ret


def rotate_key(key, deg):
    if deg == 1:
        return rotate_90(key)
    elif deg == 2:
        return rotate_180(key)
    elif deg == 3:
        return rotate_270(key)
    else:
        return key
        
       
def solution(key, lock):
    key = np.array(key)
    lock = np.array(lock)
    a = np.r_[np.zeros(lock.shape), np.zeros(lock.shape), np.zeros(lock.shape)]
    b = np.r_[np.zeros(lock.shape), lock, np.zeros(lock.shape)]
    lock_large = np.c_[a, b, a]
    lock_s = lock.shape[0]
    key_s = key.shape[0]
    for i in range(4):
        key_r = rotate_key(key, i)
        for off_x in range(lock_s * 3 - key_s):
            for off_y in range(lock_s * 3 - key_s):
                # lock_large와 key를 겹친다
                temp_large = lock_large.copy()
                temp_large[off_y:off_y+key_s, off_x:off_x+key_s] = temp_large[off_y:off_y+key_s, off_x:off_x+key_s] + key_r
                temp_cen = temp_large[lock_s:lock_s * 2, lock_s:lock_s * 2]
                if np.all(temp_cen == 1):
                    print(key_r)
                    return True
    return False
