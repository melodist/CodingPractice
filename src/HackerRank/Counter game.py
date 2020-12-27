"""
https://www.hackerrank.com/challenges/counter-game/problem
Using bit manipulation
"""
#1. My Solution
def counterGame(n):
    binary = format(n, 'b')
    i = len(binary) - 1
    cnt = 0
    while i > 0 and binary[i] == '0':
        cnt += 1
        i -= 1
    
    cnt += binary[:i].count('1') + 1
            
    return 'Richard' if cnt % 2 == 1 else 'Louise'
