"""
https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem
Using greedy algorithm
"""
#1. My Solution
def decentNumber(n):
    if n < 3:
        print(-1)
        return
    
    three = 0
    while n >= 3:
        if n % 3 != 0:
            n -= 5
            three += 5
        else:
            print('5' * n + '3' * three)
            return
            
    
    print(-1 if n != 0 else '3' * three)
    
