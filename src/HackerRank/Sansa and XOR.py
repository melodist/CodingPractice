"""
https://www.hackerrank.com/challenges/sansa-and-xor/problem
XOR is associative
For arr = [i, i, i, ..., i] if num(arr) is even, i^i^...^i = 0
"""
def sansaXor(arr):
    if len(arr) % 2 == 0:
        return 0
    else:
        even = arr[0::2]
        temp = 0
        for num in even:
            temp ^= num
        return temp
