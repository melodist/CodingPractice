"""
https://programmers.co.kr/learn/courses/30/lessons/84325
Implementation Problem
"""
#1. My Solution
from collections import defaultdict


def solution(table, languages, preference):
    answer = ''
    jobs = [] # 직업군 이름
    scores = [] # 직업군 언어 점수
    result = [] # 개발자 선호 직업군 점수

    # 직군별 점수 계산
    for i, r in enumerate(table):
        r = r.split()
        jobs.append(r[0])
        scores.append(defaultdict(int))
        for j in range(5):
            scores[i][r[j+1]] = 5 - j

    # 선호 직업군 정렬 (점수, 직군)
    for k in range(5):
        score = 0
        for l, p in zip(languages, preference):
            score += scores[k][l] * p
        result.append((score, jobs[k]))

    # 점수 내림차순, 직군 오름차순
    result.sort(key= lambda x: (-x[0], x[1]))  

    return result[0][1]

#2. Other Solution
def solution(table, languages, preference):
    score = {}
    for t in table:
        for lang, pref in zip(languages, preference):
            if lang in t.split():
                score[t.split()[0]] = score.get(t.split()[0], 0) +  (6 - t.split().index(lang)) * pref
    return sorted(score.items(), key = lambda item: [-item[1], item[0]])[0][0]
