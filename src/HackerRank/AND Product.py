"""
https://www.hackerrank.com/challenges/and-product/problem
Using Bit Manipulation
1. Find the bits where a and b differ using XOR
2. Mask out all lower bits than 1
"""
#1. My Solution
def andProduct(a, b):
    x = (1 << int(math.log2(a^b))) - 1
    y = 2**32 - 1 - x

    return a & y
