"""
https://programmers.co.kr/learn/courses/30/lessons/68936
Using divide and conquer
"""
#1. My Solution
def solution(arr):
    def func(r_s, r_e, c_s, c_e):
        if r_s == r_e:
            return (0, 1) if arr[r_s][c_s] else (1, 0)

        r_mid = (r_s + r_e) // 2
        c_mid = (c_s + c_e) // 2
        lu_0, lu_1 = func(r_s, r_mid, c_s, c_mid)
        ru_0, ru_1 = func(r_s, r_mid, c_mid+1, c_e)
        ld_0, ld_1 = func(r_mid+1, r_e, c_s, c_mid)
        rd_0, rd_1 = func(r_mid+1, r_e, c_mid+1, c_e)
        total_0 = lu_0 + ru_0 + ld_0 + rd_0
        total_1 = lu_1 + ru_1 + ld_1 + rd_1

        if total_0 == 0:
            return (0, 1)
        elif total_1 == 0:
            return (1, 0)
        else:
            return (total_0, total_1)

    return func(0, len(arr)-1, 0, len(arr)-1)
