"""
https://programmers.co.kr/learn/courses/30/lessons/84512
Using product
"""
#1. My Solution
from itertools import product


def solution(word):
    chars = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    for i in range(5):
        [words.append(''.join(w)) for w in product(chars, repeat = i+1)]
        
    return sorted(words).index(word) + 1
