"""
https://www.hackerrank.com/challenges/stepping-stones-game
Algebra Problem

If there is x meets condition, 
x(x+1)/2 = n
(x+1/2)^2 - (1/2)^2 = 2*n
x+1/2 = sqrt(2*n + 1/4)
x = sqrt(2*n + 1/4) - 1/2 = (sqrt(8*n + 1) - 1)/2
"""
#1. My Solution
def solve(n):
    return 'Go On Bob '+ str(int(((1 + 8*n)**0.5 - 1)/2)) if ((1 + 8*n)**0.5 - 1)/2 == ((1 + 8*n)**0.5 - 1)//2 else "Better Luck Next Time"
