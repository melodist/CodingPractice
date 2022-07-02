"""
Using recursion and bitwise calculation
"""
#1. My Solution (33ms)
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: return 0
        if k <= 2**(n-2):
            return self.kthGrammar(n-1, k) & 1
        else:
            return ~self.kthGrammar(n-1, k - 2**(n-2)) & 1
        
#2. Other Solution (23ms)
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        if self.kthGrammar(n-1, (k+1)//2):
            return (0,1)[k%2]
        return (1,0)[k%2]
