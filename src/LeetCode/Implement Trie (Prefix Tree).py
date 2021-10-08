"""
https://leetcode.com/problems/implement-trie-prefix-tree/
Using Trie
"""
#1. My Solution
class Trie:

    def __init__(self):
        self.trie = dict()

    def insert(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] = dict()
            curr = curr[c]
        curr['/0'] = '/0'
        
    def search(self, word: str) -> bool:
        curr = self.trie
        for c in word:
            if c in curr:
                curr = curr[c]
            else:
                return False

        return True if '/0' in curr else False

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for c in prefix:
            if c in curr:
                curr = curr[c]
            else:
                return False
            
        return True
