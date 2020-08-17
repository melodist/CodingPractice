"""
https://programmers.co.kr/learn/courses/30/lessons/42893/
Using Regular Expression and string parsing
Consider the case which has multiple external links on single line
"""
import re
from collections import defaultdict


def solution(word, pages):
    n = len(pages)
    urls = [''] * n
    in_links = defaultdict(list)
    out_links = [0] * n
    basics = [0] * n
    sums = [0] * n

    for i, p in enumerate(pages):
        a = p.split('\n')
        
        # Find URL of page
        meta = re.search('<meta property="og:url" content=(.+)/>', p).group(1)
        m1 = re.search('(https://\S+)"', meta)
        url = m1.group(1)
        urls[i] = url
        
        # Find body region of page
        for j, s in enumerate(a):
            if s == '<body>':
                body_start = j
            if s == '</body>':
                body_end = j
                
        # Caution! Using findall() instead of search() to find all external links.
        for s in a[body_start+1:body_end]:
            m2 = re.findall('<a href="(\S+)"', s)
            for o in m2:
                print(o)
                in_links[o].append(i)
                out_links[i] += 1
        
        # Count basic score of page
        basics[i] = re.sub('[^a-z]+', '.', p.lower()).split('.').count(word.lower())

    for i in range(n):
        temp = 0
        for link in in_links[urls[i]]:
            temp += basics[link] / out_links[link]
        sums[i] = basics[i] + temp

    return sums.index(max(sums))
