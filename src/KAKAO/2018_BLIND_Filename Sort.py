"""
https://programmers.co.kr/learn/courses/30/lessons/17686
Using regular expression and dictionary sort
"""
#1. My Solution
import re


def solution(files):
    dic = {}
    # Divide file into head number tail
    for f in files:
        ind_h = re.match('\D+', f).end()
        head = f[:ind_h].lower()
        ind_n = ind_h + re.match('\d{1,5}', f[ind_h:]).end()
        number, tail = f[ind_h:ind_n], f[ind_n+1:]
        number = int(number)
        dic[f] = (head, number, tail)

    dic_sorted = sorted(dic.items(), key = lambda x: (x[1][0], x[1][1]))
    answer = [a[0] for a in dic_sorted]

    return answer
    
#2. Other Solution
import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d{1,5}', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b
