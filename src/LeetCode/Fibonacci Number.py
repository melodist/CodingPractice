"""
https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1661/
Using Recursion
"""
#1. My Solution (1325ms)
class Solution:
    def fib(self, n: int) -> int:
        return n if n == 0 or n == 1 else self.fib(n-2) + self.fib(n-1)
    
#2. Other Solution (35ms)
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        
        if n == 0:
            return a
        
        for i in range(1, n):
            a, b = b, a+b
            
        return b
