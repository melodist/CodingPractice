"""
https://www.hackerrank.com/challenges/ctci-ransom-note/problem
"""
from collections import defaultdict

def checkMagazine(magazine, note):
    dic_m = defaultdict(int)
    dic_n = defaultdict(int)

    for word in magazine:
        dic_m[word] += 1

    for word in note:
        dic_n[word] += 1

    for key in dic_n.keys():
        if dic_m[key] < dic_n[key] or key not in dic_n:
            print('No')
            return
    
    print('Yes')
