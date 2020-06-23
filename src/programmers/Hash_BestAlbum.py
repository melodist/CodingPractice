"""
https://programmers.co.kr/learn/courses/30/lessons/42579
"""
#1. My Solution
from collections import defaultdict


def solution(genres, plays):
    dict_g = defaultdict(int)
    dict_p = defaultdict(dict)
    n = len(genres)
    
    for i in range(n):
        dict_g[genres[i]] += plays[i]
        dict_p[genres[i]][i] = plays[i]
        
    answer = []
    sorted_g = sorted(dict_g.items(), key = lambda x: x[1], reverse=True)
    
    for genre, _ in sorted_g:
        sorted_p = sorted(dict_p[genre].items(), key = lambda x: x[1], reverse=True)
        if len(sorted_p) > 1:
            answer.append(sorted_p[0][0])
            answer.append(sorted_p[1][0])
        else:
            answer.append(sorted_p[0][0])

    return answer
    
#2. Solution without defaultdict
def solution(genres, plays):
    # Make empty list for each genre
    dic = {g:[] for g in set(genres)}
    
    # Store the plays for each music
    for a in zip(genres, plays, range(len(genres))):
        dic[a[0]].append((a[1], a[2]))
        
    answer = []
    # Sort genre for sum of musics
    # genre x / music y
    g_sort = sorted(list(dic.keys()), key = lambda x: sum(map(lambda y: y[0], dic[x])), reverse=True)
    for g in g_sort:
        # Sort index for plays and indexes
        temp = [a[1] for a in sorted(dic[g], key = lambda x: (x[0], x[1]), reverse=True)]
        answer += temp[:min(len(temp), 2)]

    return answer
