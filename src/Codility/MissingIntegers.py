"""
https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
Using Hashmap
"""
def solution(A):
    # write your code in Python 3.6
    dic = {}
    for num in A:
        dic[num] = 0
    i = 1
    while True:
        if i not in dic.keys():
            return i
            break
        i += 1
