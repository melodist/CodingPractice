"""
https://www.hackerrank.com/challenges/service-lane/problem
"""
def serviceLane(n, cases):
    return list(map(lambda i: min(width[i[0]:i[1]+1]), cases))
