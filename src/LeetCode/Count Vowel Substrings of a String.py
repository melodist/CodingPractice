"""
https://leetcode.com/contest/weekly-contest-266/problems/count-vowel-substrings-of-a-string/
Implementation Problem
"""
#1. My Solution (64ms)
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        answer = 0
        for i in range(n):
            if word[i] in vowel:
                temp = set()
                temp.add(word[i])
                for j in range(i+1, n):
                    if word[j] in vowel:
                        temp.add(word[j])
                        if len(temp) == 5:
                            answer += 1
                    else:
                        break
                        
        return answer
    
#2. Other Solution (31ms)
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans = 0 
        freq = defaultdict(int)
        for i, x in enumerate(word): 
            if x in "aeiou": 
                if not i or word[i-1] not in "aeiou": 
                    jj = j = i # set anchor
                    freq.clear()
                freq[x] += 1
                while len(freq) == 5 and all(freq.values()): 
                    freq[word[j]] -= 1
                    j += 1
                ans += j - jj
        return ans 
