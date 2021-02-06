"""
https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3
Implementation Problem
"""
#1. My Solution
import re


def solution(new_id):
    #1 upper to lower
    new_id = new_id.lower()
    #2
    new_id = ''.join(re.findall('[a-z0-9-_.]' ,new_id))
    #3 and 4
    new_id = '.'.join([c for c in new_id.split('.') if c])
    #5
    new_id = new_id if new_id else 'a'
    #6
    new_id = new_id[:15] if len(new_id) > 15 else new_id
    new_id = new_id[:-1] if new_id[-1] == '.' else new_id
    #7
    new_id = new_id + new_id[-1] * (3 - len(new_id)) if len(new_id) < 3 else new_id
    
    return new_id
    
#2. Other Solution
# re.sub(pattern, repl, string, count, flags)
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
