"""
https://www.hackerrank.com/challenges/sum-vs-xor/problem
Math problem
Calculate 0 in binary form of n
"""
#1. Solution using built-in function
def sumXor(n):
    x = format(n, 'b').count('0')
    return 2**x if n > 0 else 1
    
#2. Solution using bitwise calculation
def sumXor(n):
    x = 0
    while n > 0:
        if n % 2 == 0:
            x += 1
        n>>=1
        
    return 2**x
