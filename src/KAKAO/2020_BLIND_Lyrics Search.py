"""
https://programmers.co.kr/learn/courses/30/lessons/60060
Using trie
"""
#1. Solution using trie
def solution(words, queries):
    trie_by_length = [({}, {}) for _ in range(10001)]
    for word in words:
        length = len(word)
        t = trie_by_length[length][0]
        for c in word:
            t['count'] = t.get('count', 0) + 1
            t.setdefault(c, {})
            t = t[c]
        t = trie_by_length[length][1]
        for c in word[::-1]:
            t['count'] = t.get('count', 0) + 1
            t.setdefault(c, {})
            t = t[c]
    ans = []
    for query in queries:
        length = len(query)
        if query[0] == '?':
            t = trie_by_length[length][1]
            query = query[::-1]
        else:
            t = trie_by_length[length][0]
        for c in query:
            if c == '?':
                ans.append(t.get('count', 0))
                break
            if c not in t:
                ans.append(0)
                break
            t = t[c]
    return ans
    
#2. Solution using counter (Timeout in TC2-4, TC2-5)
# If query or words become longer, access time will be slower
# because one trie stores (# of words) * (length of each words)
from collections import defaultdict


def solution(words, queries):
    answer = []
    trie_by_length = [({}, {}) for _ in range(10001)]
    for w in words:
        temp_f = ''
        temp_r = ''
        n = len(w)
        t0 = trie_by_length[n][0]
        t1 = trie_by_length[n][1]
        for c, d in zip('*' + w, '*' + w[::-1]):
            temp_f += c
            temp_r += d
            if temp_f not in t0:
                t0[temp_f] = 0
            if temp_r not in t1:
                t1[temp_r] = 0
            t0[temp_f] += 1
            t1[temp_r] += 1
    
    for q in queries:
        m = len(q)
        if q[0] == '?':
            t = trie_by_length[m][1]
            q1 = '*' + q.split('?')[-1][::-1]
        else:
            t = trie_by_length[m][0]
            q1= '*' + q.split('?')[0]
            
        if q1 in t:
            answer.append(t[q1])
        else:
            answer.append(0)

    return answer
