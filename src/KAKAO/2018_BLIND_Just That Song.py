"""
https://programmers.co.kr/learn/courses/30/lessons/17683/
Implementation Problem
Using regular expression and tokenizing
"""
#1. My Solution
import re

# calculate running time of music
def running_time(start, end):
    h_s, m_s = map(int, start.split(':'))
    h_e, m_e = map(int, end.split(':'))
    return (h_e - h_s) * 60 + m_e - m_s

# iterate string s for running time t
def iterate(s, t):
    n = len(s)
    q, r = divmod(t, n)
    return s * q + s[:r]

def solution(m, musicinfos):
    transfer = {'C#':'H', 'D#':'I', 'F#':'J', 'G#':'K', 'A#':'L'}
    for k, v in transfer.items():
        m = m.replace(k, v)
    answer_time = 0
    answer = '(None)'
    for s in musicinfos:
        start, end, musicname, melody = s.split(',')
        for k, v in transfer.items():
            melody = melody.replace(k, v)
        # print(start, end, musicname, melody)
        t = running_time(start, end)
        # print(t)
        melody_iter = iterate(melody, t)
        # print(melody_iter)
        if re.search(m, melody_iter) and answer_time < t:
            answer = musicname
            answer_time = t

    return answer
