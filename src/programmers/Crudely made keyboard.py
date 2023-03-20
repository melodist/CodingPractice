"""
https://school.programmers.co.kr/learn/courses/30/lessons/160586
Using dict
"""
#1. My Solution
def solution(keymap, targets):
    keys = dict()
    for k in keymap:
        for i, c in enumerate(k):
            if c not in keys:
                keys[c]  = i+1
            else:
                keys[c] = min(keys[c], i+1)
                
    ans = []
    for t in targets:
        temp = 0
        for c in t:
            if c not in keys:
                temp = -1
                break
            else:
                temp += keys[c]
                
        ans.append(temp)
        
    return ans
