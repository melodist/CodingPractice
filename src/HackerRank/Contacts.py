"""
https://www.hackerrank.com/challenges/contacts/problem
"""
#1. My Solution using trie
def contacts(queries):
    class Node(object):
        def __init__(self, key, data=None):
            self.key = key
            self.data = None
            self.count = 0
            self.children = {}

    class Trie(object):
        def __init__(self):
            self.head = Node(None)

        def insert(self, s):
            cur = self.head

            for c in s:
                if c not in cur.children:
                    cur.children[c] = Node(c)

                cur = cur.children[c]
                cur.count += 1

            cur.data = s

        def starts_with(self, s):
            cur = self.head

            for c in s:
                if c not in cur.children:
                    return 0
                cur = cur.children[c]

            return cur.count
                
    t = Trie()
    result = []
    for q, s in queries:
        if q == 'add':
            t.insert(s)
        else:
            result.append(t.starts_with(s))
            
    return result
    
#2. Other solution using counter
from collections import Counter

cter = Counter()
for i in xrange(int(raw_input().strip())):
    cmd, word = raw_input().strip().split(' ')
    if cmd == 'add':
        for i in xrange(1, len(word) + 1):
            cter.update([word[0:i]])
    else:
        print cter[word]
