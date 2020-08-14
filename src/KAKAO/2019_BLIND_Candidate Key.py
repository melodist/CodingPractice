"""
https://programmers.co.kr/learn/courses/30/lessons/42890
Find Uniqueness and minimality seperately
"""
from itertools import combinations


def minimality(keys, candidates):
    if len(keys) == 1:
        return True

    all_combinations = []
    for r in range(1, len(keys)):
        combinations_object = combinations(keys, r)
        combinations_list = list(combinations_object)
        all_combinations += combinations_list

    for comb in all_combinations:
        if comb in candidates:
            return False

    return True


def solution(relation):
    cols = len(relation[0])
    rows = len(relation)
    candidates = set()
    answer = 0

    items = [x for x in range(cols)]
    all_combinations = []

    for r in range(1, cols+1):
        combinations_object = combinations(items, r)
        combinations_list = list(combinations_object)
        all_combinations += combinations_list
    
    
    for keys in all_combinations:
        if minimality(keys, candidates):
            # Check uniqueness
            temp = [''] * rows
            for k in keys:
                for i in range(rows):
                    temp[i] += " " + relation[i][k]
            if len(temp) == len(set(temp)):
                candidates.add(keys)

    return len(candidates)
