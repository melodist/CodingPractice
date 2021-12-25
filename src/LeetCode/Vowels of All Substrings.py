"""
https://leetcode.com/contest/weekly-contest-266/problems/vowels-of-all-substrings/
For each vowels s[i],
it could be in the substring starting at s[x] and ending at s[y],
where 0 <= x <= i and i <= y < n,
that is (i + 1) choices for x and (n - i) choices for y.

So there are (i + 1) * (n - i) substrings containing s[i].
"""
#1. My Solution (140ms)
class Solution:
    def countVowels(self, word: str) -> int:
        return sum((i + 1) * (len(word) - i) for i, c in enumerate(word) if c in 'aeiou')
