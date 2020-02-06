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
