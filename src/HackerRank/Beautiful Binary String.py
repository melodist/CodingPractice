"""
https://www.hackerrank.com/challenges/beautiful-binary-string/problem
Using greedy algorithm
"""
#1. My Soltuion
def beautifulBinaryString(b):
    n = len(b)
    ans = 0
    i = 2
    while i < n:
        if b[i] == '0' and b[i-1] == '1' and b[i-2] == '0':
            i += 2
            ans += 1
        i += 1

    return ans
    
#2. Solution using replace()
def beautifulBinaryString(b):
    return (len(b)  - len(b.replace("010", ""))) // 3
