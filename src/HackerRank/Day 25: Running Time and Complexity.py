"""
https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
Checks if n is divisible by 2 or any odd number from 3 to sqrt(n)
"""
import sys

def isPrime(n):
    if n == 2: return True # 2 is divisible by 2
    if (n == 1) or (n & 1 == 0): return False 
    
    root_n = int(n**0.5)
    for i in range(3, root_n+2, 2):
        if n % i == 0:
            return False
        
    return True
 
n = int(input())
a = [int(sys.stdin.readline()) for _ in range(n)]
   
for t in a:
    if isPrime(t):
        print('Prime')
    else:
        print('Not prime')
