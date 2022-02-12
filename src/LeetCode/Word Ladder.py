"""
https://leetcode.com/problems/word-ladder
Using BFS
"""
#1. My Solution (787ms)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0
        
#2. Optimal Solution (137ms)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        begin_set = set([beginWord])
        end_set = set([endWord])
        length = 2
        word_len = len(beginWord)
        visited = set()
        while begin_set:
            if len(begin_set) > len(end_set):
                # switch to small one to traverse from other end
                begin_set, end_set = end_set, begin_set
            
            next_begin_set = set()
            for word in begin_set:
                word_chars = list(word)
                for i in range(word_len):
                    for c in string.ascii_lowercase:
                        old_char = word_chars[i]
                        word_chars[i] = c
                        next_word = "".join(word_chars)
                        if next_word in end_set:
                            return length
                        if next_word not in visited and next_word in wordList:
                            next_begin_set.add(next_word)
                            visited.add(next_word)
                        word_chars[i] = old_char
                        
            begin_set = next_begin_set
            length += 1
    
        return 0
