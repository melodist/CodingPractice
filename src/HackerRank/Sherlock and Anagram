"""
https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
Using Hashmap
Brute Force Problem
"""
from collections import Counter


def sherlockAndAnagrams(s):
    answer = 0
    for i in range(1, len(s)):
        maps = Counter()
        for j in range(0, len(s)-i+1):
            maps[''.join(sorted(s[j:i+j]))] += 1

        for key in maps.keys():
            if maps[key] > 1:
                answer += (maps[key] - 1) * maps[key] // 2

    return answer
