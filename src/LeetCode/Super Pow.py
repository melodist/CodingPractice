"""
https://leetcode.com/problems/super-pow
Using recursion and modulo distributive property
"""
#1. My Solution (222ms)
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def pow(a, k):
            if k == 0: return 1
            a %= base

            if k % 2 == 1:
                return (a * pow(a, k-1)) % base
            else:
                sub = pow(a, k/2)
                return (sub * sub) % base

        if not b: return 1
        last = b.pop()
        base = 1337

        part1 = pow(a, last)
        part2 = pow(self.superPow(a, b), 10)

        return (part1 * part2) % base

#2. Simple Solution (84ms)
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a,int(''.join(map(str,b))),1337)
