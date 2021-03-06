"""
https://www.hackerrank.com/challenges/reverse-shuffle-merge/problem
Using greedy algorithm

1. Built frequency hash-map for char and occurences. Original word has half of the occurence of every char
2. Reverse the original string and try to construct the smallest lexicographic one
3. While iterating, use a stack (the idea somehow resembles the largest rectangle problem, from stack category).
4. If the new char occurs already n/2 times, where n = frequency of the original / 2, 
then skip this char, since we can not, nor we should push it to the stack
5. else pop chars from the stack, if: stack is not empty, 
top char stack is greater than the new char and by removing the top char we still can build the word with desired frequency
"""
#1. My Solution
from collections import defaultdict


def frequency(s):
    res = defaultdict(int)
    for char in s:
        res[char] += 1
    return res


def reverseShuffleMerge(s):
    char_freq = frequency(s)  # store freq of char in s
    used_chars = defaultdict(int)  # count char used in res
    remain_chars = dict(char_freq)  # copy char_freq
    res = []
    
    def can_use(char):
        return (char_freq[char] // 2 - used_chars[char]) > 0
    
    # Check char can be popped from res
    def can_pop(char):
        needed_chars = char_freq[char] // 2
        return used_chars[char] + remain_chars[char] - 1 >= needed_chars
    
    for char in reversed(s):
        if can_use(char):
            # Make lexicographically smallest word
            while res and res[-1] > char and can_pop(res[-1]):
                removed_char = res.pop()
                used_chars[removed_char] -= 1
            
            used_chars[char] += 1
            res.append(char)
        
        remain_chars[char] -= 1
    
    return "".join(res)
