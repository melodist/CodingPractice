"""
https://www.hackerrank.com/challenges/kangaroo/
"""
def kangaroo(x1, v1, x2, v2):
    dist = x2 - x1
    steps = v1 - v2
    if steps > 0:
        if dist % steps == 0:
            return('YES')
    
    return('NO')
