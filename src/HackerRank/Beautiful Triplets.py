"""
https://www.hackerrank.com/challenges/beautiful-triplets/problem
"""
def beautifulTriplets(d, arr):
    INT_MAX = 20001
    a = [0] * INT_MAX
    ans = 0
    for i in arr:
        a[i] = 1
    for i in arr[:-2]:
        if a[i] == 1:
            if i+d < INT_MAX and a[i+d] == 1 :
                if i+2*d < INT_MAX and a[i+2*d] == 1:
                    ans += 1

    return ans
