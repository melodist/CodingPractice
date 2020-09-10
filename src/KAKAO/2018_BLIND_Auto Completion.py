"""
https://programmers.co.kr/learn/courses/30/lessons/17685
"""
#1. Solution using defaultdict (Timeout in Python 3)
from collections import defaultdict


def solution(words):
    answer = 0

    cter = defaultdict(int)
    for word in words:
        temp = ''
        for c in word:
            temp += c
            cter[temp] += 1

    for word in words:
        temp = ''
        for c in word:
            answer += 1
            temp += c
            if cter[temp] == 1:
                break

    return answer
    
#2. Solution using Trie
# Faster than solution1 in longer string
# ex) ["aaaa...aaaab", "aaaa...aaaac"]
from collections import deque


class Node():
    def __init__(self, value):
        self.value = value
        self.n = 0
        self.child = {}

class Trie():
    def __init__(self):
        self.head = Node('\0')
        
    def add(self, word):
        cur = self.head
        for c in word:
            cur.n += 1
            if c not in cur.child:
                cur.child[c] = Node(c)
            cur = cur.child[c]
            
    def solve(self):
        answer = 0
        q = deque(self.head.child.values())
        while q:
            cur = q.popleft()
            answer += cur.n
            if cur.n == 1:
                continue
            
            for c in cur.child:
                q.append(cur.child[c])
                
        return answer

    
def solution(words):
    trie = Trie()
    for word in words:
        trie.add(word+'\0')
        
    return trie.solve()

#3. Other Solution using sort
# Sort the array lexicographically and compare adjacent words
def solution(words):
    answer = 0
    words.sort()
    for idx, word in enumerate(words):
        res = 1
        if idx > 0:
            for i, char in enumerate(word):
                res = max(res, i+1)
                if len(words[idx-1]) == i or words[idx-1][i] != char: break
        if idx+1 < len(words):
            for i, char in enumerate(word):
                res = max(res, i+1)
                if len(words[idx+1]) == i or words[idx+1][i] != char: break
        answer += res

    return answer
