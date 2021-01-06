"""
https://www.hackerrank.com/challenges/cipher/problems
Using bit manipulation
i: 012...
s: ABC...
ans:abcdefg...
ans: abcdefg...
ans[i] = s[i] ^ accum, accum ^= ans[i]
"""
#1. My Solution
def cipher(k, s):
    l = []
    ans = ''
    accum = 0
    for i in range(len(s)-k+1):
        l.append(accum ^ int(s[i]))
        accum ^= int(l[-1])
        if i >= k-1:
            accum ^= int(l[i-k+1])
        ans += str(l[i])

    return ans
