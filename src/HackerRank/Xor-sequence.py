"""
https://www.hackerrank.com/challenges/xor-se/problem
Using XOR
0 ^ a = a, a ^ a = 0
A1 = 1, A2 = 1 ^ 2, A3 = 1 ^ 2 ^ 3
Let Bi = A0 ^ A1 ^ ... ^ Ai
Bi for even = 2 ^ 4 ^ 6 ^ ... ^ i = (1 ^ 2 ^ 3 ^ ... ^ i/2) * 2
Bi for odd = 1 ^ 3 ^ 5 ^ ... ^ i = (1 ^ 2 ^ 3 ^ ... ^ (i-1)/2) * 2 + X
X = 1 ^ 1 ^ ... ^ 1 (repeated i times) = 1 if i is odd / 0 if i is even

bitmask(K)00 = 4K
bitmask(K)01 = 4K+1
bitmask(K)10 = 4K+2
bitmask(K)11 = 4K+3
"""
#1. My Solution
def xorSequence(l, r):
    def G(x):
        r = x % 8
        if r == 0 or r == 1:
            return x
        elif r == 2 or r == 3:
            return 2
        elif r == 4 or r == 5:
            return x+2
        else:
            return 0
    
    return G(r) ^ G(l-1)
