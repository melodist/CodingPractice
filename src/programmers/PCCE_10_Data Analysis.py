"""
https://school.programmers.co.kr/learn/courses/30/lessons/250121
Implementation Problem
"""
#1. My Solution
def solution(data, ext, val_ext, sort_by):
    columns = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    filtered_data = filter(lambda x: x[columns[ext]] < val_ext, data)
    filtered_list = list(filtered_data)
    filtered_list.sort(key=lambda x: x[columns[sort_by]])
    return filtered_list
